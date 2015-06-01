from django.conf.urls import patterns, url
from blog.views import PostList


urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^posts/$', PostList.as_view(), name='posts'),
    url(r'^category/(?P<slug>\w+)/$', 'blog.views.category', name='category'),
    url(r'^(?P<slug>\w+)/$', 'blog.views.post_detail', name='post_detail'),
)
