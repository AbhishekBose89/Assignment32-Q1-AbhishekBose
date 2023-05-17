from rest_framework import serializers
from .models import Rating
from .models import Products
from .models import Order


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    rating = RatingSerializer()

    class Meta:
        model = Products
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer()

    class Meta:
        model = Order
        fields = "__all__"
