from django.shortcuts import render
from django.views.generic import ListView
from blog.models import BlogPost


class IndexView(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'blog/index.html'
