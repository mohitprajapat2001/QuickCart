# -*- coding: utf-8 -*-
from django.db import models
from django_extensions.db.models import ActivatorModel, TitleDescriptionModel


class Banner(TitleDescriptionModel, ActivatorModel):
    banner_image = models.ImageField(
        verbose_name="Banner Image", upload_to="Banner Images", null=True, blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Banner Details"
        ordering = ["id"]
