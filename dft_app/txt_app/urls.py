from . import views
from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', views.index, name='index')]
