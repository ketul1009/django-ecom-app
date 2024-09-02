from django.shortcuts import get_object_or_404
from .models import Category
from product.models import Product
from variant.models import Variant
from django.http import JsonResponse

# Create your views here.
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