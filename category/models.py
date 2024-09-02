from django.db import models

# Create your models here.
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