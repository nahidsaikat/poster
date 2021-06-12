from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()

router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<pk>/upload/', PostFileView.as_view({'post': 'create'}), name='post-file-upload'),
]
