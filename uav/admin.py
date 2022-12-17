from django.contrib import admin

from uav.models import UAV, Model, Brand


# Register your models here.
class UAVAdmin(admin.ModelAdmin):
    fields = (
        "name",
        "model",
        "weight",
        "color"
    )


class BrandAdmin(admin.ModelAdmin):
    fields = (
        "name",
        "uav",
        "founded_at"
    )


class ModelAdmin(admin.ModelAdmin):
    fields = (
        "name",
    )


admin.site.register(UAV, UAVAdmin)
admin.site.register(Model, ModelAdmin)
admin.site.register(Brand, BrandAdmin)
