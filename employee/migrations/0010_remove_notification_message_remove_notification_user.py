# Generated by Django 5.0.1 on 2024-04-15 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_alter_notification_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='message',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='user',
        ),
    ]
