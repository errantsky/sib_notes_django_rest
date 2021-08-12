from autoslug import AutoSlugField
from django.conf import settings
from django.db import models
from django.urls import reverse


# Create your models here.
class Folder(models.Model):
    name = models.CharField("Name of Folder", max_length=255)
    slug = AutoSlugField(
        "Folder Address",
        unique=True,
        always_update=False,
        populate_from="name",
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("folders:detail", kwargs={"slug": self.slug})
