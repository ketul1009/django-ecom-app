from django.http import JsonResponse
from .models import Collection
from variant.models import Variant
from django.shortcuts import render, get_object_or_404
from product.views import product_list
from variant.views import variant_list
import json

def get_collections(request):
    #return all products
    collections = Collection.objects.all()  # Get all products
    collection_list = [
        {
            'title': collection.title,
            'published': collection.published,
            'updated_at': collection.updated_at,
        }
        for collection in collections
    ]
    return JsonResponse(collection_list, safe=False)

def get_collection(request, id):

    collection = get_object_or_404(Collection, id=id)
    products = collection.product.all()
    request_body = json.loads(request.body.decode("utf-8"))
    if(request_body['type']=='variant'):
        variants = Variant.objects.filter(product__in=products)
        data = {
            'id': collection.id,
            'name': collection.title,
            'variants': variant_list(variants)
            # 'description': collection.description,    
            # Add more fields as needed
        }
    
    else:
        data = {
            'id': collection.id,
            'name': collection.title,
            'products': product_list(products)
            # 'description': collection.description,    
            # Add more fields as needed
        }

    return JsonResponse(data,safe=True)