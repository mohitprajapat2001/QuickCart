# -*- coding: utf-8 -*-
# Generated by Django 5.0.6 on 2024-05-15 16:36

import django.db.models.deletion
import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Offer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="title")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="description"),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Inactive"), (1, "Active")],
                        default=1,
                        verbose_name="status",
                    ),
                ),
                (
                    "activate_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="keep empty for an immediate activation",
                        null=True,
                    ),
                ),
                (
                    "deactivate_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="keep empty for indefinite activation",
                        null=True,
                    ),
                ),
                (
                    "discount",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=10,
                        null=True,
                        verbose_name="Discount Percentage",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="title")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="description"),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Inactive"), (1, "Active")],
                        default=1,
                        verbose_name="status",
                    ),
                ),
                (
                    "activate_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="keep empty for an immediate activation",
                        null=True,
                    ),
                ),
                (
                    "deactivate_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="keep empty for indefinite activation",
                        null=True,
                    ),
                ),
                (
                    "subcategory",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subcategories",
                        to="products.category",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="title")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="description"),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Inactive"), (1, "Active")],
                        default=1,
                        verbose_name="status",
                    ),
                ),
                (
                    "activate_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="keep empty for an immediate activation",
                        null=True,
                    ),
                ),
                (
                    "deactivate_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="keep empty for indefinite activation",
                        null=True,
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=1,
                        max_digits=10,
                        null=True,
                        verbose_name="Product Price",
                    ),
                ),
                (
                    "quantity",
                    models.SmallIntegerField(
                        blank=True, default=1, null=True, verbose_name="Product Quanity"
                    ),
                ),
                (
                    "category",
                    models.ManyToManyField(
                        related_name="product", to="products.category"
                    ),
                ),
                (
                    "offer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product",
                        to="products.offer",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ProductImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image_1",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="Product Images",
                        verbose_name="Product Image 1",
                    ),
                ),
                (
                    "image_2",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="Product Images",
                        verbose_name="Product Image 2",
                    ),
                ),
                (
                    "image_3",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="Product Images",
                        verbose_name="Product Image 3",
                    ),
                ),
                (
                    "image_4",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="Product Images",
                        verbose_name="Product Image 4",
                    ),
                ),
                (
                    "product",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_images",
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]
