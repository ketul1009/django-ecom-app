from rest_framework import serializers
from .models import Product, Variant, Collection, Category, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['source', 'alt_text', 'updated_at']

class VariantSerializer(serializers.ModelSerializer):
    product_title = serializers.CharField(source='product.title')
    image = ImageSerializer()

    class Meta:
        model = Variant
        fields = ['product_title', 'title', 'created_at', 'updated_at', 'available_for_sale', 'price', 'image']

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    variants = VariantSerializer(many=True)

    class Meta:
        model = Product
        fields = ['title', 'description', 'created_at', 'updated_at', 'images', 'variants']

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['title', 'published', 'updated_at']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'created_at', 'updated_at']
