# Generated by Django 5.0.7 on 2024-07-21 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articleApp', '0006_alter_comment_created_at'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='articletag',
            unique_together={('article', 'tag')},
        ),
    ]
