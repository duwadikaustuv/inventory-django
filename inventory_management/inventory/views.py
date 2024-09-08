from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Category, Supplier, Item, Project, ItemUsage
from .serializers import CategorySerializer, SupplierSerializer, ItemSerializer, ProjectSerializer, ItemUsageSerializer
from django.http import HttpResponse

# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Supplier ViewSet
class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

# Item ViewSet with filtering and sorting
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['category', 'supplier', 'name', 'item_code']  # Filtering by category, supplier, name, and item_code
    ordering_fields = ['name', 'price', 'item_code', 'quantity']  # Sorting by name, price, item_code, and quantity

# Low Stock ViewSet for handling low-stock alerts
class LowStockItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter(quantity__lt=10)  # Low-stock threshold set to 10
    serializer_class = ItemSerializer

# Project ViewSet with filtering and sorting
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name', 'manager', 'item_taken', 'item_code']  # Filtering by project name, manager, etc.
    ordering_fields = ['name', 'manager', 'item_taken', 'item_code']  # Sorting by project name, etc.

# ItemUsage ViewSet for handling item requests and returns
class ItemUsageViewSet(viewsets.ModelViewSet):
    queryset = ItemUsage.objects.all()
    serializer_class = ItemUsageSerializer

def home(request):
    return HttpResponse("Hello World")