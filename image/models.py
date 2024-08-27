from django.db import models
from product.models import Product

# Create your models here.
class Image(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    source = models.URLField(max_length=200)
    alt_text = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return Product.objects.get(id=self.product_id.id).title
        