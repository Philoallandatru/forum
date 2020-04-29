from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        fields = ("content", "post")
        model = Comment
    
    def __init__(self,*args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        # if user is not None:
        #     self.files[]

# class CommentPostForm(forms.ModelForm):
#     class Meta:
#         fields = ("content", "post")
#         model = Comment



class  CommentPostForm(forms.Form):
    content = forms.CharField(max_length=100)


