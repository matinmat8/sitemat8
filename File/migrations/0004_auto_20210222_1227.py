# Generated by Django 3.1.5 on 2021-02-22 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('File', '0003_auto_20210220_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_file',
            name='File',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
