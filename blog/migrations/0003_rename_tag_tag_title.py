# Generated by Django 3.2.7 on 2021-09-13 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210913_0654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tag',
            new_name='title',
        ),
    ]
