# Generated by Django 5.0.7 on 2024-07-21 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleApp', '0005_comment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2024-01-01'),
            preserve_default=False,
        ),
    ]
