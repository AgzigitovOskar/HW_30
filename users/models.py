from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Location(models.Model):
    name = models.CharField(max_length=200, unique=True)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)

    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return self.name


class UserRoles(models.TextChoices):
    MEMBER = "member", _("member")
    MODERATOR = "moderator", _("moderator")
    ADMIN = "admin", _("admin")


class User(AbstractUser):
    role = models.CharField(choices=UserRoles.choices, max_length=9)
    age = models.PositiveSmallIntegerField()
    location = models.ManyToManyField(Location, null=True, blank=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username

