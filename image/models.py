from django.db import models
from product.models import Product
from variant.models import Variant

# Create your models here.
class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    variant = models.OneToOneField(Variant, on_delete=models.CASCADE, related_name='image', null=False)
    source = models.URLField(max_length=200)
    alt_text = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{Product.objects.get(id=self.product.id).title}"
        