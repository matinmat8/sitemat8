from django import forms
from .models import PostComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('name', 'email', 'body')


class PostSearch(forms.Form):
    search = forms.CharField()


class share_post_email(forms.Form):
    name = forms.CharField(max_length=60)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)