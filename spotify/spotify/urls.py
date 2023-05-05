from django.contrib import admin
from django.urls import path, include
from asosiy.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("qoshiqchilar", QoshiqchiViewSet)
router.register("albomlar", AlbomViewSet)
router.register("qoshiqlar", QoshiqViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('qoshiqlar/', QoshiqlarAPIView.as_view()),
    # path('albomlar/', AlbomlarAPIView.as_view()),
    path('', include(router.urls)),
    path('albomlar/<int:pk>/qoshiq/', AlbomViewSet.as_view({'get': 'qoshiq'}), name='qoshiq'),

    path('qoshiqchi/<int:pk>/', QoshiqchiDetailAPIView.as_view()),
]
