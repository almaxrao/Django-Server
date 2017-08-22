from django.db import models
# Create your models here.


'''
class Bucketlist(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
'''

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
