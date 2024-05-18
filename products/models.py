# -*- coding: utf-8 -*-
from django.db import models
from django_extensions.db.models import (
    ActivatorModel,
    TimeStampedModel,
    TitleDescriptionModel,
)
from users import models as userModel


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

    class Meta:
        verbose_name = "Product Category"
        ordering = ["id"]


class Offer(TitleDescriptionModel, ActivatorModel, TimeStampedModel):
    image = models.ImageField(
        upload_to="Offer Images", null=True, blank=True, max_length=1024
    )
    discount = models.DecimalField(
        verbose_name="Discount Percentage",
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        userModel.CustomUser, on_delete=models.CASCADE, related_name="offers"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="offer"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Offer"
        ordering = ["id"]


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
    user = models.ForeignKey(
        userModel.CustomUser,
        on_delete=models.CASCADE,
        related_name="product",
        null=True,
        blank=True,
    )
    offer = models.ForeignKey(
        Offer, on_delete=models.CASCADE, related_name="product", null=True, blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="product",
        null=True,
        blank=True,
    )
    view_count = models.PositiveIntegerField(default=0, verbose_name="View Count")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
        ordering = ["id"]


class Review(TimeStampedModel):
    user = models.ForeignKey(
        userModel.CustomUser,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="review",
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True, related_name="review"
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return "Review for {} By {}".format(self.product, self.user)

    class Meta:
        verbose_name = "Products Review"
        ordering = ["created"]


class ProductImage(models.Model):
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name="product_images"
    )
    image_1 = models.ImageField(
        verbose_name="Product Image 1",
        upload_to="Product Images",
        null=True,
        blank=True,
        max_length=1024,
    )
    image_1_alt = models.CharField(
        max_length=4096, verbose_name="Image 1 Alt Text", null=True, blank=True
    )
    image_2 = models.ImageField(
        verbose_name="Product Image 2",
        upload_to="Product Images",
        null=True,
        blank=True,
        max_length=1024,
    )
    image_2_alt = models.CharField(
        max_length=4096, verbose_name="Image 2 Alt Text", null=True, blank=True
    )

    image_3 = models.ImageField(
        verbose_name="Product Image 3",
        upload_to="Product Images",
        null=True,
        blank=True,
        max_length=1024,
    )
    image_3_alt = models.CharField(
        max_length=4096, verbose_name="Image 3 Alt Text", null=True, blank=True
    )

    image_4 = models.ImageField(
        verbose_name="Product Image 4",
        upload_to="Product Images",
        null=True,
        blank=True,
        max_length=1024,
    )
    image_4_alt = models.CharField(
        max_length=4096, verbose_name="Image 4 Alt Text", null=True, blank=True
    )

    def __str__(self):
        return "{} - Product Images".format(self.product.title)

    class Meta:
        verbose_name = "Product Images"
        ordering = ["id"]
