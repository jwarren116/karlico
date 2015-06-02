from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from blog.models import BlogPost, Image, Category


# class IndexView(ListView):
#     model = BlogPost
#     context_object_name = 'posts'
#     template_name = 'blog/index.html'
#     queryset = BlogPost.objects.filter(display=True).order_by('-created')[:5]


def index(request):
    posts = BlogPost.objects.filter(display=True).order_by('-created')[:5]
    categories = Category.objects.all()
    return render(request, 'blog/index.html', {
        'posts': posts,
        'categories': categories,
    })


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = BlogPost.objects.filter(display=True).filter(category=category)
    return render(request, 'blog/posts.html', {
        'posts': posts,
    })


# class PostView(DetailView):
#     model = BlogPost
#     context_object_name = 'post'
#     template_name = 'blog/detail.html'
#     queryset = BlogPost.objects.filter(display=True)


def post_detail(request, category, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    images = Image.objects.filter(post=post)
    return render(request, 'blog/detail.html', {
        'post': post,
        'images': images,
    })


class PostList(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'blog/posts.html'
    queryset = BlogPost.objects.filter(display=True).order_by('-created')
