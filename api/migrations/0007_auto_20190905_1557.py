# Generated by Django 2.2.4 on 2019-09-05 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_thread_last_poster'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='replies',
            new_name='total_posts',
        ),
    ]
