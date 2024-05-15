# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from schema_graph.views import Schema

urlpatterns = [
    path("admin/", admin.site.urls),
    path("schema/", Schema.as_view()),
]
