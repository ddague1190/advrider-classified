# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from advrider_django.bikes.models import Category, Manufacturer, Image, Bike

class Bike(DjangoItem):
    django_model = Bike

class AdvriderClassifiedItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
