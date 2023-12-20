# myneBlog/views.py
from django.views.generic import ListView, DetailView 
from .models import Post
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

class myneBlogListView(ListView):
    model = Post
    template_name = 'home.html'

class myneBlogDetailView(DetailView): # новое
    model = Post
    template_name = 'post_detail.html'


class myneBlogCreateView(CreateView): # новое изменение
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']
class myneBlogUpdateView(UpdateView): # Новый класс
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
class myneBlogDeleteView(DeleteView): # Создание нового класса
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

#@login_required
def c_logout(request):
    logout(request)
    return redirect("home")