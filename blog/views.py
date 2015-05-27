from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import BlogPost, Image


class IndexView(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'blog/index.html'
    queryset = BlogPost.objects.filter(display=True).order_by('-created')[:5]


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
