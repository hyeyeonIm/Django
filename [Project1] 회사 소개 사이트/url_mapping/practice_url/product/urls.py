from django.urls import path
from product import views

urlpatterns = [
    path('', views.productlist),   # 즉 http://127.0.0.1:8000/product/
    path('first/', views.productfirst),
]
