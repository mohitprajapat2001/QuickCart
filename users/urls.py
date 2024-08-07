# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from schema_graph.views import Schema
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("home/", include("users.urls")),
]

urlpatterns = urlpatterns + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
