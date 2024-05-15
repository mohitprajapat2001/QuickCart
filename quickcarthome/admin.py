# -*- coding: utf-8 -*-
from django.contrib import admin
from django_extensions.db.models import ActivatorModel
from quickcarthome.models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "status",
    ]
    readonly_fields = ["id"]
    fieldsets = [
        (
            "Banner Details",
            {
                "fields": ["id", "title", "description", "status"],
            },
        ),
        (
            "Banner Image",
            {
                "fields": ["banner_image"],
            },
        ),
    ]
    search_fields = [
        "title",
    ]
    list_filter = ["status"]
    ordering = ["title"]
    actions = ["status_unactive", "status_active"]

    @admin.display(description="Unavtive Selected Users")
    def status_unactive(self, request, queryset):
        queryset.update(status=ActivatorModel.INACTIVE_STATUS)

    @admin.display(description="Active Selected Users")
    def status_active(self, request, queryset):
        queryset.update(status=ActivatorModel.ACTIVE_STATUS)
