from django.urls import path
from .views import *
from django.urls import re_path

urlpatterns = [

     path('shops_details/<int:pk>/', ShopDetailAPIView.as_view()),

]