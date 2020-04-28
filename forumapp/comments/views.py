from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic
from django.contrib.auth import get_user_model
from .models import Comment
from braces.views import SelectRelatedMixin

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