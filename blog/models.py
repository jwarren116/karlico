from django.db import models


class Category(models.Model):
    category = models.CharField('Category', max_length=63, unique=True)
    slug = models.SlugField('URL Slug', max_length=63, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.category

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('blog.views.category', args=[str(self.slug)])


class BlogPost(models.Model):
    title = models.CharField('Title', max_length=127, unique=True)
    slug = models.SlugField('URL Slug', max_length=127, unique=True)
    content = models.TextField('Content')
    category = models.ForeignKey(Category)
    created = models.DateTimeField('Created', auto_now_add=True, auto_now=False)
    display = models.BooleanField('Display on Blog?', default=False)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('blog.views.post_detail', args=[str(self.category.slug), str(self.slug)])


class Image(models.Model):
    post = models.ForeignKey(BlogPost)
    image = models.ImageField('Image', upload_to='img')
    caption = models.TextField('Caption')

    def __unicode__(self):
        return self.caption


class About(models.Model):
    content = models.TextField('About Me')

    class Meta:
        verbose_name_plural = 'About'

    def __unicode__(self):
        return self.content


class Link(models.Model):
    name = models.CharField('Name of Site', max_length=63)
    link = models.URLField('Link')
    about = models.ForeignKey(About)
