from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subcategories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_descendants(self):
        descendants = [self]
        children = Category.objects.filter(parent=self)
        print(children)
        for child in children:
            descendants.append(child)
            descendants.extend(child.get_descendants())

        return descendants

class Product(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # TODO:
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, related_name='products')

    def __str__(self):
        #comment added to check git workflow on main branch
        #this is to check if experimental changes are visible
        return self.title
    
class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    available_for_sale = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.product.title} {self.title}"

class Collection(models.Model):
    title = models.CharField(max_length=200)
    published = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.ManyToManyField(Product, related_name='collection')

    def __str__(self):
        return self.title
    
class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    variant = models.OneToOneField(Variant, on_delete=models.CASCADE, related_name='image', null=False)
    source = models.URLField(max_length=200)
    alt_text = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{Product.objects.get(id=self.product.id).title}"
    