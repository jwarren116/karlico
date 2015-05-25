from django.db import models


class BlogPost(models.Model):
    title = models.CharField('Title', max_length=63)
    content = models.TextField('Content')
    created = models.DateTimeField('Created', auto_now_add=True, auto_now=False)
    display = models.BooleanField('Display on Blog?', default=False)

    def __unicode__(self):
        return self.title


class Image(models.Model):
    post = models.ForeignKey(BlogPost, related_name='images')
    image = models.ImageField('Image', upload_to='img')
    caption = models.TextField('Caption')

    def __unicode__(self):
        return self.caption
