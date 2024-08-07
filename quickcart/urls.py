# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from schema_graph.views import Schema
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", RedirectView.as_view(url="/home")),
    path("home/", include("quickcarthome.urls")),
    path("category/", include("products.urls")),
    path("schema/", Schema.as_view()),
]

urlpatterns = urlpatterns + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
