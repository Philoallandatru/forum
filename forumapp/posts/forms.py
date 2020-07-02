from django import forms
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        fields = ("message", "group")
        model = models.Post


    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        self.fields['message'].label = "发帖内容"
        self.fileds["group"].label = "板块"
        super().__init__(*args, **kwargs)
        if user is not None:

            # you can only post to group you joined 
            self.fields["group"].queryset = (
                models.Group.objects.filter(
                    pk__in=user.groups.values_list("group__pk")
                )
            )


class SearchForm(forms.Form):
    group_name = forms.CharField()

class CommentPostForm():
    pass