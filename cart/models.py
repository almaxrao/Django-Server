from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


# Create your models here.


class UserCart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    user_cart=models.IntegerField(blank=True, null=True)
    cart_products = ArrayField(

            models.IntegerField(blank=True),

    )



User.profile = property(lambda u:UserCart.objects.get_or_create(user=u)[0])