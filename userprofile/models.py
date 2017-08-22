from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class UserProfile2(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    user_address = models.TextField(blank=True, null=True)
    user_phone = models.IntegerField(blank=True, null=True)



User.profile = property(lambda u:UserProfile2.objects.get_or_create(user=u)[0])