from django.forms import ModelForm
from .models import Upload_File


class Upload_file(ModelForm):
    class Meta:
        model = Upload_File
        fields = ['name', 'email', 'subject_project', 'example', 'phone_number', 'BudgetAmount', 'File']

