# myneBlog/views.py
from django.views.generic import ListView, DetailView 
from .models import Post
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .form import (
    ClientCreationForm, 
    ClientAuthenticationForm, 
    ReviewForm
)

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

@login_required
def c_logout(request):
    logout(request)
    return redirect("home")

def c_register(request):
    if request.user.is_authenticated:
        return redirect("products_list")

    if request.method == "POST":
        form = ClientCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("products_list")
    else:
        form = ClientCreationForm()
    return render(request, "signup.html", {"form": form})

def c_login(request):
    if request.user.is_authenticated:
        return redirect("products_list")

    if request.method == "POST":
        form = ClientAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get("next", "products_list")
            return redirect(next_url)
    else:
        form = ClientAuthenticationForm()
    return render(request, "login.html", {"form": form})