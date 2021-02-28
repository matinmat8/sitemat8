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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['search'].widget.attrs.update({'class': 'form-control', 'exampleInputEmail1': 'search in posts'})


class share_post_email(forms.Form):
    name = forms.CharField(max_length=60)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        help_texts = {
            'name': 'name of projects',
            'email': 'Email address',
            'to': 'Enter the email address you want to send this post to',
            'comments': 'Write your comment about this post'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'your name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email address'})
        self.fields['to'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter the email address you '
                                                                                       'want to send this post to'})
        self.fields['comments'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Write your comment about this post'})