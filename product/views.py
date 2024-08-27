from django.http import JsonResponse
from .models import Product

def product_list(request):
    #return all products
    products = Product.objects.all()  # Get all products
    product_list = [
        {
            'title': product.title,
            'description': product.description,
            'created_at': product.created_at,
            'updated_at': product.updated_at,
            'images': [image.source for image in product.images.all()]
        }
        for product in products
    ]
    return JsonResponse(product_list, safe=False)
