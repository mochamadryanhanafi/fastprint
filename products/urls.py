from django.urls import path
from django.views.generic import RedirectView
from .views import (
    ProductListView,
    ProductView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

urlpatterns = [
    path('api/products/', ProductListView.as_view(), name='product_list_api'),
    path('', ProductView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products', RedirectView.as_view(pattern_name='product_list')),
    path('products/', RedirectView.as_view(pattern_name='product_list')),
]
