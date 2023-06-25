from django.urls import path
from board import views

urlpatterns = [
    path('', views.board),   # 즉 http://127.0.0.1:8000/board/
    path('first/', views.boardfirst),
]
