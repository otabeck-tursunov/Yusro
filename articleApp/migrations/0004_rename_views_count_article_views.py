# Generated by Django 5.0.7 on 2024-07-21 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articleApp', '0003_rename_articles_count_category_articles_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='views_count',
            new_name='views',
        ),
    ]
