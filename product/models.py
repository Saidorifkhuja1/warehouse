from django.db import models
from django.utils import timezone
from warehouse.models import Warehouse


class Product(models.Model):
    name = models.CharField(max_length=250)
    cost = models.IntegerField()
    amount = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    add_time = models.DateTimeField(default=timezone.now)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    def __str__(self):
            return self.name


class SoldProduct(models.Model):
    name = models.CharField(max_length=250)
    cost = models.IntegerField()
    amount = models.IntegerField()
    note = models.TextField(null=True, blank=True)
    add_time = models.DateTimeField(default=timezone.now)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



