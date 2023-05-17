from django.db import models

# Create your models here.


class Rating(models.Model):
    rate = models.DecimalField(max_digits=6, decimal_places=2)
    count = models.IntegerField(null=True, blank=True)


class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=200)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, related_name="rating")


class Order(models.Model):
    products = models.ManyToManyField(Products, related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.TextField()
    subtotal = models.DecimalField(max_digits=25, decimal_places=2)
