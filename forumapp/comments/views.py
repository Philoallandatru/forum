from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic
from django.contrib.auth import get_user_model
from .models import Comment
from braces.views import SelectRelatedMixin
from django.views.generic import View
from .forms import CommentPostForm
from posts.models import Post

# Create your views here.
User = get_user_model()

class DeleteComment(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = Comment
    select_related = ("user", "group")
    success_url = reverse_lazy("posts:all")

class CommentList(generic.ListView):
    model = Comment
    select_related = ("post")


class CommentDetail(generic.DetailView):
    model = Comment
    template_name = "comments/comment_detail.html"


class CreateComment(LoginRequiredMixin, generic.CreateView, SelectRelatedMixin):
    fields = ('content', 'post')
    model = Comment

    # this set the user of your create comment form
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class UserComment(generic.ListView):
    model = Comment

    def get_queryset(self):
        try:
            self.comment_user = User.objects.prefetch_related("comments").get(
                username__iexact = self.kwargs.get("username")
            )
        except User.DoestNotExist:
            raise Http404
        else:
            return self.comment_user.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_user'] = self.comment_user
        return context;


class  CommentPostCreate(View):
    # def get(self, request):
    #     form = CommentPostForm()
    #     return render(request, 'posts/post_detail.html', {'form' : form})

    def  post(self,request,pk,username):
        post = Post.objects.get(id=pk)
        comment_content = request.POST.get('content')
        comment = Comment()
        comment.post = post
        comment.user = User.objects.get(username=username)
        comment.content=comment_content
        comment.save()
        return redirect(post.get_absolute_url())
        # return  reverse(post.get_absolute_url())


