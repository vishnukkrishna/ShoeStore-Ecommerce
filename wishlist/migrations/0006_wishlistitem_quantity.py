# Generated by Django 4.1.7 on 2023-04-01 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0005_remove_wishlistitem_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlistitem',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
