# Generated by Django 5.0.1 on 2024-03-29 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('employee', '0005_remove_notification_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='cug', related_query_name='custom_user_group', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='notification',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='cup', related_query_name='custom_user_permission', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
