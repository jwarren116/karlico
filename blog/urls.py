from django.conf.urls import patterns, url
from blog.views import PostList


urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^(?P<pk>\d+)/$', 'blog.views.post_detail', name='post_detail'),
    url(r'^posts/$', PostList.as_view(), name='posts'),
    url(r'^(?P<category>\w+)/$', 'blog.views.category', name='category'),
)
