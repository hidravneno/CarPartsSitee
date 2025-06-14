from django.db import models

class Part(models.Model):
    CATEGORY_CHOICES = [
        ('Engine', 'Engine'),
        ('Brakes', 'Brakes'),
        ('Suspension', 'Suspension'),
        ('Electrical', 'Electrical'),
        ('Interior', 'Interior'),
        ('Body', 'Body'),
        ('Tires', 'Tires'),
        ('Motor oil','Motor oil'),

    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='parts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

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

