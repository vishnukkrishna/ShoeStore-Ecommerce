# Generated by Django 4.1.7 on 2023-04-01 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0004_wishlistitem_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlistitem',
            name='user',
        ),
    ]
