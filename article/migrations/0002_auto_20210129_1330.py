# Generated by Django 3.1.5 on 2021-01-29 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postarticle',
            options={'ordering': ('-publish',)},
        ),
    ]