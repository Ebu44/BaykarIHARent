from django.urls import path
from rest_framework.routers import DefaultRouter

from uav.api.views import UAVViewSet, ModelViewSet, BrandViewSet

router = DefaultRouter()
router.register("uav", UAVViewSet, basename="UAV")
router.register("model", ModelViewSet, basename="Model")
router.register("brand", BrandViewSet, basename="Brand")

urlpatterns = router.urls
