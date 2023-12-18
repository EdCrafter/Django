
# blog_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('blog.urls')), # новое изменение
=======
    path('accounts/', include('django.contrib.auth.urls')), # Добавили новый маршрут
    path('', include('blog.urls')),
>>>>>>> e6773e8ad4adff6f00de6fa0b26767a18abb548f
]