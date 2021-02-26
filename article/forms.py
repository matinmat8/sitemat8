from os import name

from django import forms
from .models import PostComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('name', 'email', 'body')

        #def __init__(self, *args, **kwargs):
        #    super().__init__(*args, **kwargs)
        #    self.fields[name].widget.attrs.update({'class': 'form-control'})
        #    self.fields[email].widget.attrs.update({'class': 'form-control'})
        #   self.fields[body].widget.attrs.update({'class': 'form-control'})

        #widgets = {
         #   'name': forms.TextInput(attrs={'class': 'form-control'}),
          #  'email': forms.EmailField(attrs={'class': 'form-control'}),
           # 'body': forms.Textarea(attrs={'class': 'form-control'}),
        #}


class PostSearch(forms.Form):
    search = forms.CharField()


class share_post_email(forms.Form):
    name = forms.CharField(max_length=60)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)