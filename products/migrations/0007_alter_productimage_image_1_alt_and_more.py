# -*- coding: utf-8 -*-
# Generated by Django 5.0.6 on 2024-05-16 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0006_remove_product_category_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productimage",
            name="image_1_alt",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Image 1 Alt Text"
            ),
        ),
        migrations.AlterField(
            model_name="productimage",
            name="image_2_alt",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Image 2 Alt Text"
            ),
        ),
        migrations.AlterField(
            model_name="productimage",
            name="image_3_alt",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Image 3 Alt Text"
            ),
        ),
        migrations.AlterField(
            model_name="productimage",
            name="image_4_alt",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Image 4 Alt Text"
            ),
        ),
    ]