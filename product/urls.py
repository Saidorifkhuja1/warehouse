from django.urls import path
from .views import *

urlpatterns = [
    path('products_create/', ProductCreateView.as_view()),
    path('products_list/', ProductListView.as_view()),
    path('products_detail/<int:pk>/', ProductDetailView.as_view()),
    path('products_update/<int:pk>/', ProductUpdateView.as_view()),
    path('products_delete/<int:pk>/', ProductDeleteView.as_view()),
]
