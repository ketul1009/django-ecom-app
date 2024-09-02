from django.http import JsonResponse
from .models import Product

def get_products(request):
    #return all products
    products = Product.objects.all()  # Get all products
    data = product_list(products)
    return JsonResponse(data, safe=False)

def product_list(products):
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
    return product_list