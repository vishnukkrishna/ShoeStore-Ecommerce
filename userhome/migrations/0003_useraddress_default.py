# Generated by Django 4.1.7 on 2023-03-16 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userhome', '0002_useraddress_full_name_useraddress_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='default',
            field=models.BooleanField(default=False),
        ),
    ]
