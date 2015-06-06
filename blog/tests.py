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


class TestHomeView(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.post = PostFactory.create()
        self.about = AboutFactory.create()
        super(TestHomeView, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(TestHomeView, self).tearDown()

    def test_home(self):
        '''test that home page is available to visitor'''
        self.selenium.get(self.live_server_url)
        assert self.selenium.find_element_by_id('about')
        assert self.selenium.find_element_by_class('post')
