from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView
)

app_name = 'product'

urlpatterns = [
    path('', ProductListView.as_view(), name = 'product-list'),
    path('<int:my_id>/', ProductDetailView.as_view(), name = 'product-detail'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('<int:my_id>/update/', ProductUpdateView.as_view(), name="product-update"),
    path('<int:my_id>/delete/', ProductDeleteView.as_view(), name = 'product-delete')
]