from django.contrib import admin
from .models import Manufacturer, Category, Bike, Image


admin.site.register(Manufacturer)
admin.site.register(Category)
admin.site.register(Bike)
admin.site.register(Image)
