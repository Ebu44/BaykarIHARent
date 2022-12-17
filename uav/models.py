from django.db import models

# Create your models here.


class Model(models.Model):
    name = models.CharField(verbose_name="Name", max_length=64)
    updated_at = models.DateTimeField(verbose_name="Updated At", auto_now=True)
    created_at = models.DateTimeField(verbose_name="Created At", auto_now_add=True)

    def __str__(self):
        return self.name


class UAV(models.Model):
    class ColorChoices(models.TextChoices):
        BLUE = 'BU', 'Blue'
        RED = 'RD', 'Red'
        GREEN = 'GR', 'Green'
        WHITE = 'WT', 'White'

    name = models.CharField(verbose_name="Name", max_length=64)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    weight = models.IntegerField(verbose_name="Weight")
    color = models.CharField(
        verbose_name="Color",
        choices=ColorChoices.choices,
        default=ColorChoices.WHITE,
        max_length=12
    )

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(verbose_name="Name", max_length=64)
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)
    founded_at = models.DateField(verbose_name="Founded At")

    def __str__(self):
        return self.name
