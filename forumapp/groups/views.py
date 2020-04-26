from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from groups.models import Group,GroupMember
from . import models
from django.shortcuts import render, HttpResponse

# render /templates/groups/group_form
class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ("name", "description")
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group

def Search(request):
    if request.method == 'POST':
        group_name = request.POST['group_name']
        group_list = Group.objects.filter(name = group_name)
        if len(group_list) == 0:
            return render(request, 'groups/group_search_not_found.html', {})
        else:
            link = group_list[0].get_absolute_url()
            return render(request, 'groups/groups_search.html', {'group_name' : group_name, 'link' : link})


class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get("slug"))

        try:
            GroupMember.objects.create(user=self.request.user,group=group)

        except IntegrityError:
            messages.warning(self.request,("提示：你已经是{}讨论组的成员了".format(group.name)))

        else:
            messages.success(self.request,"你现在是{}讨论组的一员了！   .".format(group.name))

        return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        try:
            membership = models.GroupMember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get("slug")
            ).get()

        except models.GroupMember.DoesNotExist:
            messages.warning(
                self.request,
                "你还没有加入这个VN讨论组，不能离开。"
            )

        else:
            membership.delete()
            messages.success(
                self.request,
                "你已离开了这个VN讨论组。"
            )
        return super().get(request, *args, **kwargs)
