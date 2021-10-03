from django.db import models

# Create your models here.


class Page (models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    title = models.CharField(max_length=255, blank=False)

class Content (models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    h1 = models.CharField(max_length=255, blank=True)
    h2 = models.CharField(max_length=255, blank=True)
    text = models.TextField(max_length=2048, blank=True)