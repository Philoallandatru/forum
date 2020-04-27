from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        fields = ("content", "post")
        model = Comment
    
    def __ini__(self,*args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        # if user is not None:
        #     self.files[]