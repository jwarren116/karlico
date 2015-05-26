from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import BlogPost


class IndexView(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'blog/index.html'


class PostView(DetailView):
    model = BlogPost
    context_object_name = 'post'
    template_name = 'blog/detail.html'
