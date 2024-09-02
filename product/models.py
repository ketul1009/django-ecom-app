from django.db import models
from category.models import Category
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, related_name='products')

    def __str__(self):
        #comment added to check git workflow on main branch
        #this is to check if experimental changes are visible
        return self.title
