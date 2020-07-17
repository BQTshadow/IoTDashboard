from django.contrib import admin

# Register your models here.
from .models import Humidity, Temperature

admin.site.register(Humidity)
admin.site.register(Temperature)
