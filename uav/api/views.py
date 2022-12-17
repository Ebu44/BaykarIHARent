from rest_framework import mixins, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from uav.api.serializers import UAVSerializer, ModelSerializer, BrandSerializer
from uav.models import UAV, Model, Brand


class UAVViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = UAV.objects.all()
    permissions = (IsAuthenticated,)
    serializer_class = UAVSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    search_fields = ["^name", "model__name"]
    ordering_fields = ['name', "model__name", 'weight', "color"]

    def get_permissions(self):
        if self.action == "list":
            self.permissions = [AllowAny,]
        return super().get_permissions()


class ModelViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = Model.objects.all()
    permissions = (IsAuthenticated,)
    serializer_class = ModelSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    search_fields = ["^name"]
    ordering_fields = ['name', "updated_at", 'created_at']

    def get_permissions(self):
        if self.action == "list":
            self.permissions = [AllowAny,]
        return super().get_permissions()


class BrandViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = Brand.objects.all()
    permissions = (IsAuthenticated,)
    serializer_class = BrandSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    search_fields = ["^name"]
    ordering_fields = ['name', "uav__name", 'founded_at']

    def get_permissions(self):
        if self.action == "list":
            self.permissions = [AllowAny,]
        return super().get_permissions()
