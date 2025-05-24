from django.db import models

class Part(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='parts/', blank=True, null=True)
    category = models.CharField(max_length=100, default='Uncategorized')  # Agrega un valor predeterminado
    created_at = models.DateTimeField(auto_now_add=True)  # Agrega este campo para registrar la fecha de creación

    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

    class Meta:
        permissions = [
            ("view_inventory", "Can view inventory"),
            ("manage_inventory", "Can add or delete inventory"),
        ]

