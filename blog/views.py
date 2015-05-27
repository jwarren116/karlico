from django.views.generic import ListView, DetailView
from blog.models import BlogPost


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


class PostList(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'blog/posts.html'
    queryset = BlogPost.objects.filter(display=True).order_by('-created')
