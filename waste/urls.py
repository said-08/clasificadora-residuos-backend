from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'waste', views.WasteView, 'waste')

urlpatterns = [
  path("api/", include(router.urls))
]