from django.contrib import admin
from web import models
# Register your models here.
admin.site.register(models.Page)
admin.site.register(models.Content)
admin.site.register(models.UToken)
admin.site.register(models.Social)
admin.site.register(models.Background)