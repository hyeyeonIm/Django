"""
URL configuration for helloworld project.

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
from django.urls import path
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.home, name='hello_world'),  # http://127.0.0.1:8000/ 에 대해서 요청이 들어온다면 
    # myapp안에 있는 views.py에 있는 home을 실행시켜라
    # name='hello_world' : url의 이름

    path('test/', myapp.views.test, name='hello-world'),

    # path('/test', FUNCTION),  # http://127.0.0.1:8000/test 에 어떤 요청이 들어온다면 FUNCTION이라는 함수를 실행시켜라
]


# 현재 웹서비스 주소 : http://127.0.0.1:8000/ 는 내 컴퓨터를 지칭한다.
# 요칭이 http://127.0.0.1:8000/1 에 대해서도 들어올 수 있고
# http://127.0.0.1:8000/abc/1 에 대해서도 들어올 수 있다.