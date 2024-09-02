from django.urls import path
from .views import *

urlpatterns = [
    path("collections/", get_collections, name="collection_list"),
    path("collection/<int:id>", get_collection, name='collection')
]