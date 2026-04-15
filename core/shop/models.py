from django.db import models
from django.contrib.auth.models import User
import uuid


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    contact = models.CharField(max_length=15)
    address = models.TextField()

    custom_id = models.CharField(max_length=10, unique=True, blank=True)

    def __str__(self):
        return self.user.username
    
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Hand Tools', 'Hand Tools'),
        ('Power Tools', 'Power Tools'),
        ('Measuring Tools', 'Measuring Tools'),
        ('Cutting Tools', 'Cutting Tools'),
        ('Safety Equipment', 'Safety Equipment'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    size = models.CharField(max_length=50)   # ✅ NEW
    quantity = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    
    def status(self):
        if self.quantity == 0:
            return "Out of Stock"
        elif self.quantity <= 5:
            return "Low Stock"
        return "In Stock"
