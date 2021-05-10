from django.forms import ModelForm
from .models import Upload_File
from django import forms


class Upload_file(forms.ModelForm):
    class Meta:
        model = Upload_File
        fields = ['name', 'email', 'subject_project', 'example', 'phone_number', 'BudgetAmount', 'File']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Name of project'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your email'})
        self.fields['subject_project'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Here you can '
                                                                                                    'enter a '
                                                                                                    'description of '
                                                                                                    'the project if '
                                                                                                    'you have one, If '
                                                                                                    'your description '
                                                                                                    'is long, '
                                                                                                    'you can upload a '
                                                                                                    'file'})
        self.fields['example'].widget.attrs.update({'class': 'form-control', 'placeholder': 'If you want a specific '
                                                                                            'design, you can enter '
                                                                                            'the page address'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your phone '
                                                                                                 'number'})
        self.fields['BudgetAmount'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your '
                                                                                                 'BudgetAmount'})
        self.fields['File'].widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'Upload your '
                                                                                                         'file about '
                                                                                                         'project'})