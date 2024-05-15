# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from quickcart import choice
from quickcart import constants


class CustomUser(AbstractUser):
    age = models.SmallIntegerField(null=True, blank=True)
    phone = PhoneNumberField(region="IN", blank=True, null=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    profile = models.ImageField(upload_to="User Profile", null=True, blank=True)
    role = models.CharField(
        default=constants.BUYER_CHOICE, choices=choice.USER_ROLE_CHOICES
    )
