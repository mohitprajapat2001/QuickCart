# -*- coding: utf-8 -*-
from django.contrib import admin
from products.models import Offer, Category, Product, ProductImage
from django_extensions.db.models import ActivatorModel


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "discount",
        "status",
    ]
    readonly_fields = ["id"]
    fieldsets = [
        (
            "Offer Details",
            {
                "fields": ["id", "title", "description", "discount", "status"],
            },
        ),
    ]
    search_fields = ["title", "discount"]
    list_filter = ["discount", "status"]
    ordering = ["title"]
    actions = ["status_unactive", "status_active"]

    @admin.display(description="Unavtive Selected Users")
    def status_unactive(self, request, queryset):
        queryset.update(status=ActivatorModel.INACTIVE_STATUS)

    @admin.display(description="Active Selected Users")
    def status_active(self, request, queryset):
        queryset.update(status=ActivatorModel.ACTIVE_STATUS)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "subcategory",
        "status",
    ]
    readonly_fields = ["id"]
    fieldsets = [
        (
            "Category Details",
            {
                "fields": ["id", "title", "description", "subcategory", "status"],
            },
        ),
    ]
    search_fields = ["title", "subcategory"]
    list_filter = ["subcategory", "status"]
    ordering = ["title"]
    actions = ["status_unactive", "status_active"]

    @admin.display(description="Unavtive Selected Users")
    def status_unactive(self, request, queryset):
        queryset.update(status=ActivatorModel.INACTIVE_STATUS)

    @admin.display(description="Active Selected Users")
    def status_active(self, request, queryset):
        queryset.update(status=ActivatorModel.ACTIVE_STATUS)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "price",
        "offer",
        "status",
    ]
    readonly_fields = ["id"]
    fieldsets = [
        (
            "Product Details",
            {
                "fields": [
                    "id",
                    "title",
                    "description",
                    "quantity",
                    "price",
                    "offer",
                    "status",
                ],
            },
        ),
        (
            "Product Category Details",
            {
                "fields": ["category"],
            },
        ),
    ]
    search_fields = ["title", "price"]
    list_filter = ["status"]
    ordering = ["title"]
    actions = ["status_unactive", "status_active"]

    @admin.display(description="Unavtive Selected Users")
    def status_unactive(self, request, queryset):
        queryset.update(status=ActivatorModel.INACTIVE_STATUS)

    @admin.display(description="Active Selected Users")
    def status_active(self, request, queryset):
        queryset.update(status=ActivatorModel.ACTIVE_STATUS)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ["id", "product"]
    readonly_fields = ["id"]
    fieldsets = [
        (
            "Product Details",
            {
                "fields": ["id", "product"],
            },
        ),
        (
            "Product Images Details",
            {
                "fields": ["image_1", "image_2", "image_3", "image_4"],
            },
        ),
    ]
    search_fields = ["product"]
    ordering = ["id"]
