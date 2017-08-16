from django.conf import settings
from django.db import models


# Create your models here.
class Organization(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class OrganizationLink(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    title = models.CharField(max_length=100, blank=True)
    organization = models.ForeignKey(Organization)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.title or self.link


