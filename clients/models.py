from django.utils import timezone
from django.db import models


class Client(models.Model):
    name = models.CharField(blank=True, max_length=255)
    email = models.EmailField(blank=True)
    country = models.CharField(blank=True, max_length=255)
    phone = models.CharField(blank=True, max_length=55)
    phone_code = models.CharField(blank=True, null=True, max_length=55)
    org = models.CharField(blank=True, max_length=255,
                           verbose_name='organisation')
    org_url = models.URLField(blank=True, verbose_name='organisation url')
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ('-modified',)
