# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.TextField(max_length=500, blank=True)
    password = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Customer(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    user_name = models.TextField(blank=True, null=True)
    user_email = models.TextField(blank=True, null=True)
    user_phone = models.IntegerField(blank=True, null=True)
    user_address = models.TextField(blank=True, null=True)
    user_password_hash = models.TextField(blank=True, null=True)
    user_purchases = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_savedlist = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_discount_code = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    product_name = models.TextField()
    product_images = models.TextField(blank=True, null=True)
    product_rating = models.FloatField(blank=True, null=True)
    product_price = models.FloatField()
    product_vendor_id = models.IntegerField(blank=True, null=True)
    product_features = models.TextField(blank=True, null=True)  # This field type is a guess.
    product_detail = models.TextField(blank=True, null=True)
    product_reviews = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'product'


class ProductOrder(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    product_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_order'


class Seller(models.Model):
    vendor_it = models.BigAutoField(primary_key=True)
    vendor_name = models.TextField()
    vendor_products_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    vendor_reviews = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'seller'
