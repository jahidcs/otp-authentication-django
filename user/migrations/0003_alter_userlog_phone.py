# Generated by Django 4.1 on 2022-08-23 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userlog_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='phone',
            field=models.CharField(max_length=11),
        ),
    ]
