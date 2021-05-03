from . import views
from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, MessageChangeViewSet


urlpatterns = [
    path('', views.index, name='index')]


router = DefaultRouter()
router.register(r'api/messages', MessageChangeViewSet, basename='MessageChange')


urlpatterns += [
    path(r'', include(router.urls)),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'message=<int:num>', MessageViewSet.as_view())]
