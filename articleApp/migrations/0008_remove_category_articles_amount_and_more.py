# Generated by Django 5.0.7 on 2024-07-27 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articleApp', '0007_alter_articletag_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='articles_amount',
        ),
        migrations.RemoveField(
            model_name='category',
            name='image_path',
        ),
        migrations.RemoveField(
            model_name='category',
            name='video_url',
        ),
    ]
