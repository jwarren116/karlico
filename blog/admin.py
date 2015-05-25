from django.contrib import admin

from blog.models import BlogPost, Image


class ImageInline(admin.StackedInline):
    model = Image
    extra = 1


class PostAdmin(admin.ModelAdmin):
    model = BlogPost
    inlines = [ImageInline]
    list_display = ('title', 'content', 'created', 'display')

admin.site.register(BlogPost, PostAdmin)
