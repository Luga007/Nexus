# Generated by Django 5.1.6 on 2025-04-08 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productview',
            name='product',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
