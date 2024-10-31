from django.urls import path
from .views import *

urlpatterns = [
    path('warehouses_create/', WarehouseCreateView.as_view()),
    path('warehouses_list/', WarehouseListView.as_view()),
    path('warehouses_details/<int:pk>/', WarehouseDetailView.as_view()),
    path('warehouse_update/<int:pk>/', WarehouseUpdateView.as_view()),
    path('warehouse_delete/<int:pk>/', WarehouseDeleteView.as_view()),


    path('categories_create/', CategoryCreateView.as_view()),
    path('categories_list/', CategoryListView.as_view()),
    path('categories/<int:pk>/', CategoryDetailView.as_view()),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view()),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view())
]
