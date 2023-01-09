from django.urls import path
from bikes.views import BikeList
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('bikes/', BikeList.as_view()),
]