# Generated by Django 3.1.5 on 2021-01-30 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_postarticle_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postarticle',
            name='file',
        ),
    ]