from django.shortcuts import render, get_object_or_404
from blog.models import BlogPost, Image, Category, About


def index(request):
    posts = BlogPost.objects.filter(display=True).order_by('-created')[:5]
    categories = Category.objects.order_by('category')
    about = About.objects.first()
    return render(request, 'blog/index.html', {
        'posts': posts,
        'categories': categories,
        'about': about,
    })


def category(request, slug):
    categories = Category.objects.order_by('category')
    category = get_object_or_404(Category, slug=slug)
    posts = BlogPost.objects.filter(display=True).filter(category=category)
    return render(request, 'blog/posts.html', {
        'posts': posts,
        'categories': categories,
    })


def post_detail(request, category, slug):
    if request.user.is_authenticated():
        post = get_object_or_404(BlogPost, slug=slug)
        images = Image.objects.filter(post=post)
    else:
        post = get_object_or_404(BlogPost, slug=slug, display=True)
        images = Image.objects.filter(post=post)
    categories = Category.objects.order_by('category')
    return render(request, 'blog/detail.html', {
        'post': post,
        'images': images,
        'categories': categories,
    })


def posts(request):
    posts = BlogPost.objects.filter(display=True).order_by('-created')
    categories = Category.objects.order_by('category')
    return render(request, 'blog/posts.html', {
        'posts': posts,
        'categories': categories,
    })
