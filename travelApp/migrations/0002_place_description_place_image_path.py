# Generated by Django 5.0.7 on 2024-07-24 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='image_path',
            field=models.ImageField(blank=True, null=True, upload_to='places/'),
        ),
    ]
