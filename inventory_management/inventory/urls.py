from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SupplierViewSet, ItemViewSet, ProjectViewSet, ItemUsageViewSet, LowStockItemViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'suppliers', SupplierViewSet, basename='supplier')
router.register(r'items', ItemViewSet, basename='item')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'item-usage', ItemUsageViewSet, basename='item-usage')
router.register(r'low-stock-items', LowStockItemViewSet, basename='low-stock-item')  # Unique basename

urlpatterns = router.urls
