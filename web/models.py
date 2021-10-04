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


class Background (models.Model):
    img = models.ImageField(upload_to='files/backgrounds/')



class Social (models.Model):
    url = models.URLField()
    html = models.CharField(blank=False, unique=True, max_length= 255)

class UToken (models.Model):
    url = models.URLField()
    name = models.CharField(blank=False, max_length=255)

