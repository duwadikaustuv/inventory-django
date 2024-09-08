from rest_framework import serializers
from .models import Category, Supplier, Item, Project, ItemUsage

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ('item_code',)  # Exclude item_code from being updated by the user

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ItemUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemUsage
        fields = '__all__'
