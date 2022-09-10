from django.db import models

# Create your models here.


class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(decimal_places=2, max_digits=11)
    procedencia = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'platos'