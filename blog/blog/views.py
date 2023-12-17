# blog/views.py
from django.views.generic import ListView, DetailView 
from .models import Post
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView): # новое
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView): # новое изменение
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']
class BlogUpdateView(UpdateView): # Новый класс
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
class BlogDeleteView(DeleteView): # Создание нового класса
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')