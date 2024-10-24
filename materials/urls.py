from django.urls import path, include
from rest_framework import routers

from materials.apps import MaterialsConfig
from materials.views import CourseViewSet

app_name = MaterialsConfig.name

router = routers.DefaultRouter()
router.register('', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]