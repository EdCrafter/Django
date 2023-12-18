# blog_project/urls.py
from django.contrib import admin
from django.urls import path, include # новое изменение

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('blog.urls')), # новое изменение
]