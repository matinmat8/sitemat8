# Generated by Django 3.1.5 on 2021-02-25 15:24

import File.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload_File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(help_text='Please describe your project', max_length=254)),
                ('subject_project', models.TextField(blank=True)),
                ('example', models.URLField(blank=True, max_length=250, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('BudgetAmount', models.IntegerField()),
                ('File', models.FileField(blank=True, upload_to='media/', validators=[File.validators.validate_file_extension])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
