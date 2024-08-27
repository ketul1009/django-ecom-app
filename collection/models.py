from django.db import models
from product.models import Product

# Create your models here.
class Collection(models.Model):
    title = models.CharField(max_length=200)
    published = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.ManyToManyField(Product, related_name='collection')

    def __str__(self):
        return self.title