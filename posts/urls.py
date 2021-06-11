from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()

router.register(r'posts', PostViewSet, basename='Posts')

urlpatterns = [
    path('', include(router.urls)),
]
