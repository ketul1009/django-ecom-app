from django.urls import path
from .views import *

urlpatterns = [
    path('category/<int:category_id>', list_by_category, name='list_by_category')
]