from django.conf.urls import patterns, include, url
from blog.views import IndexView, PostView, PostList


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', PostView.as_view(), name='post_detail'),
    url(r'^posts/$', PostList.as_view(), name='posts'),
)
