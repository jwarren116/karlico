from django.test import LiveServerTestCase
from django.core.urlresolvers import reverse
from blog.models import BlogPost, About, Category
from selenium import webdriver
import factory


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    category = 'Cats'
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
        assert self.selenium.find_element_by_class_name('post')

    def test_posts(self):
        '''test that post details and return links are available to visitor'''
        self.selenium.get(self.live_server_url)
        self.selenium.find_element_by_partial_link_text('Post Title').click()
        assert self.selenium.find_element_by_class_name('post')
        self.selenium.find_element_by_partial_link_text('Back').click()
        assert self.selenium.find_element_by_id('about')

    def test_invalid_url(self):
        '''test that invalid URL path returns custom 404 page'''
        self.selenium.get(self.live_server_url+'/posts/fake-category')
        assert self.selenium.find_element_by_class_name('container')
        self.assertIn('Page not found', self.selenium.page_source)
