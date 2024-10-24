from django.urls import path, include
from rest_framework import routers

from materials.apps import MaterialsConfig
from materials.views import CourseViewSet, LessonListAPIView, LessonUpdateAPIView, LessonCreateAPIView, \
    LessonDestroyAPIView, LessonRetrieveAPIView

app_name = MaterialsConfig.name

router = routers.DefaultRouter()
router.register('', CourseViewSet)

urlpatterns = [

    path('lessons/', LessonListAPIView.as_view(), name='lessons_list'),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lessons_retrieve'),
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lessons_create'),
    path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lessons_update'),
    path('lessons/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lessons_delete'),

]

urlpatterns += router.urls