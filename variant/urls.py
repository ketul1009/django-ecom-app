from django.urls import path
from .views import get_variants

urlpatterns = [
    path('variants/', get_variants, name='variant_list'),
]