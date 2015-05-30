from django.db import models


class Category(models.Model):
    category = models.CharField('Category', max_length=63)

    class Meta:
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.category


class BlogPost(models.Model):
    title = models.CharField('Title', max_length=63)
    content = models.TextField('Content')
    category = models.ForeignKey(Category)
    created = models.DateTimeField('Created', auto_now_add=True, auto_now=False)
    display = models.BooleanField('Display on Blog?', default=False)

    def __unicode__(self):
        return self.title


class Image(models.Model):
    post = models.ForeignKey(BlogPost)
    image = models.ImageField('Image', upload_to='img')
    caption = models.TextField('Caption')

    def __unicode__(self):
        return self.caption
