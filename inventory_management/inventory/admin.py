from django.contrib import admin
from .models import Category, Supplier, Item, Project, ItemUsage

admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Item)
admin.site.register(Project)
admin.site.register(ItemUsage)
