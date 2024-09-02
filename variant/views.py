from django.http import JsonResponse
from .models import Variant

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