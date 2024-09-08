from django.urls import path
from .views import *

urlpatterns = [
    path('products/', get_products, name='product_list'),
    path('variants/', get_variants, name='variant_list'),
    path("collections/", get_collections, name="collection_list"),
    path("collection/product/<int:id>", get_collection_product, name='collection'),
    path("collection/variant/<int:id>", get_collection_variant, name='collection'),
    path('category/<int:category_id>', list_by_category, name='list_by_category')
]