from django.test import LiveServerTestCase
from django.core.urlresolvers import reverse
from blog.models import BlogPost, About, Category
from selenium import webdriver
import factory


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    title = 'Cats'
    slug = 'cats'


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BlogPost

    title = 'Post Title'
    slug = 'post-title'
    content = 'This is a new blog post with some content'
    category = factory.SubFactory(CategoryFactory)
    display = True


class AboutFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = About

    content = 'Some interesting things about me'
