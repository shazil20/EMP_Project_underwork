# Generated by Django 5.0.1 on 2024-04-17 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0013_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]