# Generated by Django 4.2 on 2023-06-14 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection_app', '0003_alter_tracks_audio_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='subscription_expiry',
            field=models.DateField(blank=True, null=True),
        ),
    ]