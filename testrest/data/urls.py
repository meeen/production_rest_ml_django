from django.urls import path, include
from rest_framework import routers
from .views import ProductionViewSet,MachineViewSet

router = routers.DefaultRouter()
router.register("production",ProductionViewSet)
router.register("machine",MachineViewSet)

app_name = 'data'
urlpatterns = [
    path('', include(router.urls))
  ]
  