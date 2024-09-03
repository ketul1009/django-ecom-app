from django.http import JsonResponse
from .models import *
from django.shortcuts import render, get_object_or_404
import json

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

def get_variants(request):
    #return all products
    variants = Variant.objects.all()  # Get all products
    return JsonResponse(variant_list(variants), safe=False)

def variant_list(variants):

    variant_list = [
        {
            'title': f"{variant.product} {variant.title}",
            'created_at': variant.created_at,
            'updated_at': variant.updated_at,
            'available_for_sale': variant.available_for_sale,
            'price': variant.price,
            'image': variant.image.source
        }
        for variant in variants
    ]

    return variant_list

def list_by_category(request, category_id):
    
    category = get_object_or_404(Category, id=category_id)
    print(category)
    products = Product.objects.filter(category__in=category.get_descendants())
    print(products)
    variants = Variant.objects.filter(product__in=products)
    print(variants)
    data = [
        {
            'title': f"{variant.product.title} {variant.title}",
            'created_at': variant.created_at,
            'updated_at':variant.updated_at,
            'available_for_sale': variant.available_for_sale,
            'price': variant.price,
            'image': variant.image.source if variant.image else None
        }

        for variant in variants
    ]

    return JsonResponse(data, safe=False)