from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from .validators import validate_file_extension

# Create your models here.


class Upload_File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    email = models.EmailField(blank=False, help_text='Please describe your project')
    subject_project = models.TextField(blank=True)
    example = models.URLField(max_length=250, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    BudgetAmount = models.IntegerField(blank=False)
    File = models.FileField(upload_to='media/', blank=True, validators=[validate_file_extension])

    def __str__(self):
        return f'{self.user}, {self.BudgetAmount}, {self.name}'
