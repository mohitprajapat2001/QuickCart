# -*- coding: utf-8 -*-
from django.db import models
from django_extensions.db.models import (
    ActivatorModel,
    TimeStampedModel,
    TitleDescriptionModel,
)


class Offer(TitleDescriptionModel, ActivatorModel, TimeStampedModel):
    discount = models.DecimalField(
        verbose_name="Discount Percentage",
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title


class Category(TitleDescriptionModel, ActivatorModel):
    subcategory = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="subcategories",
    )

    def __str__(self):
        return self.title


class Product(TitleDescriptionModel, ActivatorModel):
    price = models.DecimalField(
        verbose_name="Product Price",
        max_digits=10,
        decimal_places=2,
        default=1,
        null=True,
        blank=True,
    )
    quantity = models.SmallIntegerField(
        verbose_name="Product Quanity", default=1, null=True, blank=True
    )
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name="product")
    category = models.ManyToManyField(Category, related_name="product")

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name="product_images"
    )
    image_1 = models.ImageField(
        verbose_name="Product Image 1",
        upload_to="Product Images",
        null=True,
        blank=True,
    )
    image_2 = models.ImageField(
        verbose_name="Product Image 2",
        upload_to="Product Images",
        null=True,
        blank=True,
    )
    image_3 = models.ImageField(
        verbose_name="Product Image 3",
        upload_to="Product Images",
        null=True,
        blank=True,
    )
    image_4 = models.ImageField(
        verbose_name="Product Image 4",
        upload_to="Product Images",
        null=True,
        blank=True,
    )

    def __str__(self):
        return "{} - Product Images".format(self.product.title)
