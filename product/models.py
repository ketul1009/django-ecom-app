from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        #comment added to check git workflow on main branch
        #return name of the product to be visible
        return self.title
