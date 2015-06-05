from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^posts/$', 'blog.views.posts', name='posts'),
    url(r'^posts/(?P<slug>[-\w]+)/$', 'blog.views.category', name='category'),
    url(r'^posts/(?P<category>[-\w]+)/(?P<slug>[-\w]+)/$', 'blog.views.post_detail', name='post_detail'),
)
