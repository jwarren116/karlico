from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import BlogPost, Image, Category


class IndexView(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'blog/index.html'
    queryset = BlogPost.objects.filter(display=True).order_by('-created')[:5]


def index(request):
    posts = BlogPost.objects.filter(display=True).order_by('-created')[:5]
    categories = Category.objects.all()
    return render(request, 'blog/index.html', {
        'posts': posts,
        'categories': categories,
    })


def category(request, category):
    post_category = Category.objects.filter(category=category)
    posts = BlogPost.objects.filter(display=True).filter(category=post_category)
    return render(request, 'blog/posts.html', {
        'posts': posts,
    })


class PostView(DetailView):
    model = BlogPost
    context_object_name = 'post'
    template_name = 'blog/detail.html'
    queryset = BlogPost.objects.filter(display=True)


def post_detail(request, pk):
    post = BlogPost.objects.filter(display=True).get(pk=pk)
    images = Image.objects.filter(post=pk)
    return render(request, 'blog/detail.html', {
        'post': post,
        'images': images,
    })


class PostList(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'blog/posts.html'
    queryset = BlogPost.objects.filter(display=True).order_by('-created')
