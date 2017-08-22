from rest_framework import serializers


'''
from .models import Bucketlist
class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Bucketlist
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
'''
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

from .models import Product
class ProductSerializer(serializers.ModelSerializer):
            class Meta:
                model = Product
                fields = ('product_name', 'product_price', 'product_detail')