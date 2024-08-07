# -*- coding: utf-8 -*-
from django.contrib import admin
from users.models import CustomUser
from django_extensions.db.models import ActivatorModel


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    date_hierarchy = "date_joined"
    list_display = ["username", "email", "role", "is_superuser", "last_login"]
    readonly_fields = ["id", "password", "date_joined", "last_login"]
    fieldsets = [
        (
            "User",
            {
                "fields": ["id", "first_name", "last_name", "username", "password"],
            },
        ),
        (
            "User Details",
            {
                "fields": ["profile", "email", "age", "phone", "address", "role"],
            },
        ),
        (
            "User Login Information",
            {
                "fields": ["date_joined", "last_login"],
            },
        ),
        (
            "User Permissions",
            {
                "fields": [
                    "is_superuser",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ],
            },
        ),
    ]
    search_fields = ["username"]
    list_filter = ["date_joined", "is_active", "is_superuser"]
    ordering = ["username"]
    actions = ["status_unactive", "status_active"]

    @admin.display(description="Unavtive Selected Users")
    def status_unactive(self, request, queryset):
        queryset.update(is_active=ActivatorModel.INACTIVE_STATUS)

    @admin.display(description="Active Selected Users")
    def status_active(self, request, queryset):
        queryset.update(is_active=ActivatorModel.ACTIVE_STATUS)
