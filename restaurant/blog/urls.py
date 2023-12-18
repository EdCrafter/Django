# blog/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    BlogListView,
    BlogUpdateView,
    BlogDetailView,
    BlogCreateView,
    BlogDeleteView, 
    c_logout,
)

urlpatterns = [
    path("logout/", c_logout, name="logout"),
    path('post/<int:pk>/delete/', # Создаем новый маршрут
    BlogDeleteView.as_view(), name='post_delete'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/',
    BlogUpdateView.as_view(), name='post_edit'),
    path('', BlogListView.as_view(), name='home'),  
]