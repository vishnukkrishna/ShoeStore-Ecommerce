# Generated by Django 4.1.7 on 2023-03-21 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_remove_color_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_colors', to='store.product'),
        ),
    ]
