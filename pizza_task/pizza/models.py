from django.db import models

# Create your models here.


class Pizza(models.Model):
    pizza_types = (
        ("Regular", "Regular"),
        ("Square", "Square"),
    )
    pizza_sizes = (
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"),
        ("Extra Large", "Extra Large")
    )
    pizza_type = models.CharField(max_length=50, choices=pizza_types, default="Regular")
    pizza_size = models.CharField(max_length=50, choices=pizza_sizes, default="Medium")
    toppings = models.CharField(max_length=50)

    def __str__(self):
        return self.pk
