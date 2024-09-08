from datetime import datetime
from django.http import JsonResponse
from .models import *
from django.shortcuts import render, get_object_or_404
import json
from django.db.models import Value
from django.db.models.functions import Concat

def get_products(request):
    #return all products
    products = Product.objects.all().values(
        'title',
        'description',
        'created_at',
        'updated_at',
        'images'
    )  # Get all products
    return JsonResponse(list(products), safe=False)

def get_collections(request):
    #return all products
    collections = Collection.objects.all().values(
        'title',
        'published',
        'updated_at'
    )  # Get all products
    return JsonResponse(list(collections), safe=False)

def get_collection_product(request, id):

    collection = get_object_or_404(Collection, id=id)
    products = collection.product.all().values(
        'title',
        'description',
        'created_at',
        'updated_at',
        'images'
    )

    return JsonResponse(list(products),safe=False)

def get_collection_variant(request, id):

    collection = get_object_or_404(Collection, id=id)
    variants = Variant.objects.select_related('product').filter(product__in=collection.product.all()).annotate(
        full_title=Concat('product__title', Value(' '), 'title')
    ).values(
        'title',  # This is the concatenated product + variant title
        'created_at',
        'updated_at',
        'available_for_sale',
        'price',
        'image__source'  # Assuming this is a URLField
    )
    return JsonResponse(list(variants), safe=False)

def get_variants(request):
    #return all products
    variants = Variant.objects.select_related('product').annotate(
        full_title=Concat('product__title', Value(' '), 'title')
    ).values(
        'title',  # This is the concatenated product + variant title
        'created_at',
        'updated_at',
        'available_for_sale',
        'price',
        'image__source'  # Assuming this is a URLField
    )
    return JsonResponse(list(variants), safe=False)

def list_by_category(request, category_id):
    
    category = get_object_or_404(Category, id=category_id)
    variants = Variant.objects.filter(product__category=category).select_related('product').values(
        'title',
        'product__title',
        'created_at',
        'updated_at',
        'available_for_sale',
        'price',
        'image__source'
    )

    # return JsonResponse(data, safe=False)
    return JsonResponse(list(variants), safe=False)