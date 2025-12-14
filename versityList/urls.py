from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import AllListViewSet

router = DefaultRouter()
router.register('list', AllListViewSet),

urlpatterns = [
    path('', include(router.urls)),
]
