from rest_framework import serializers

from uav.models import UAV, Model, Brand


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = (
            "id",
            "name",
            "updated_at",
            "created_at"
        )


class UAVSerializer(serializers.ModelSerializer):
    model = ModelSerializer()

    class Meta:
        model = UAV
        fields = (
            "id",
            "name",
            "model",
            "weight",
            "color"
        )


class BrandSerializer(serializers.ModelSerializer):
    uav = UAVSerializer()

    class Meta:
        model = Brand
        fields = (
            "id",
            "name",
            "uav",
            "founded_at"
        )
