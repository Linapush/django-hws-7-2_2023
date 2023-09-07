# Generated by Django 4.2.4 on 2023-08-28 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection_app', '0009_alter_albumgenre_created_alter_albums_created_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='albums',
            options={'ordering': ['id'], 'verbose_name': 'album', 'verbose_name_plural': 'albums'},
        ),
        migrations.AlterModelOptions(
            name='artists',
            options={'ordering': ['id'], 'verbose_name': 'artist', 'verbose_name_plural': 'artists'},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['pk'], 'verbose_name': 'client', 'verbose_name_plural': 'client'},
        ),
        migrations.AlterModelOptions(
            name='genres',
            options={'ordering': ['id'], 'verbose_name': 'genre', 'verbose_name_plural': 'genres'},
        ),
        migrations.AlterModelOptions(
            name='tracks',
            options={'ordering': ['id'], 'verbose_name': 'track', 'verbose_name_plural': 'tracks'},
        ),
    ]
