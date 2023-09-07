# Generated by Django 4.2 on 2023-06-14 13:06

import django.core.files.storage
from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('collection_app', '0004_client_subscription_expiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='artists',
            name='my_image',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location=pathlib.PurePosixPath('/home/sirius/homework_django_project/django-hws-7-2_2023/music_collection/static/audio_files')), upload_to=''),
        ),
    ]
