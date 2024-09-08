import uuid
from django.db import models

def generate_item_code():
    """Generate a unique item code."""
    return str(uuid.uuid4().hex[:8].upper())

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Supplier(models.Model):
    name = models.CharField(max_length=100, unique=True)
    contact_info = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    item_code = models.CharField(max_length=20, unique=True, default=generate_item_code, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, related_name='items')
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bill_number = models.CharField(max_length=50)
    purchase_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.item_code})"

class Project(models.Model):
    name = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=100)
    items_taken = models.ManyToManyField(Item, through='ItemUsage')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class ItemUsage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    quantity_used = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity_used} of {self.item.name} used in {self.project.name}"
