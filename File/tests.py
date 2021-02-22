from django.test import TestCase
from .models import Upload_File


# Create your tests here.


class FileTestCase(TestCase):
    Upload_File.user('login', {'username': 'MatinMat8', 'password': 'if MatinMat8'})
    Upload_File.name.create('matin')
    Upload_File.email.create('matinmat8')
    Upload_File.subject_project.create('i want a very good and big project and i send in file')
    Upload_File.example.create('https://docs.djangoproject.com/en/3.1/topics/testing/overview/')
    Upload_File.phone_number.create('e.g. +12125552368')
    Upload_File.BudgetAmount.create(50000)
