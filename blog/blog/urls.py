# myneBlog/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    myneBlogListView,
    myneBlogUpdateView,
    myneBlogDetailView,
    myneBlogCreateView,
    myneBlogDeleteView, 
    c_logout,
)

urlpatterns = [
    path("logout/", c_logout, name="logout"),
    path('post/<int:pk>/delete/', # Создаем новый маршрут
    myneBlogDeleteView.as_view(), name='post_delete'),
    path('post/new/', myneBlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', myneBlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/',
    myneBlogUpdateView.as_view(), name='post_edit'),
    path('', myneBlogListView.as_view(), name='home'),  
]