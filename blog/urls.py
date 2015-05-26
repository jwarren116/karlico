from django.conf.urls import patterns, include, url
from blog.views import IndexView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),
)
