from django.db import models

class Product(models.Model):

    product_id = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField()

    category = models.CharField(max_length=100, null=True, blank=True)
    category_id = models.CharField(max_length=50, null=True, blank=True)
    size = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField()
    price = models.IntegerField()

    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name

    from django.db import models

class RegisterUser(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

from django.db import models

class RegisterUser(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name