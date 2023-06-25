"""
URL configuration for practice_url project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first),
    path('second/', views.second),
    path('products/', include('product.urls')), # products/에 관련된 url들은 product.urls에서 담당할 것이다 (include 쓰면서)
    path('boards/', include('board.urls')),
]

# 상품 관련 url    - 아래 모든 상품 관련 url들은 product.urls에서 다룬다.
    # http://127.0.0.1:8000/products/1
    # http://127.0.0.1:8000/products/2
    # http://127.0.0.1:8000/products/3
    # http://127.0.0.1:8000/products/abc

# 구매 후기 관련 url또한 동일하다. 

