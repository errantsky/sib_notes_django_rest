from autoslug import AutoSlugField
from django.conf import settings
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel


class Note(TimeStampedModel):
    title = models.CharField("Name of Note", max_length=255)
    slug = AutoSlugField(
        "Note Address", unique=True, always_update=False, populate_from="title"
    )
    text = models.TextField("Text", blank=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=False,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("notes:detail", kwargs={"slug": self.slug})
