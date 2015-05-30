from django.contrib import admin

from blog.models import BlogPost, Image, Category


class ImageInline(admin.StackedInline):
    model = Image
    extra = 1


class PostAdmin(admin.ModelAdmin):
    model = BlogPost
    inlines = [ImageInline]
    list_display = ('title', 'category', 'content', 'created', 'display')

admin.site.register(BlogPost, PostAdmin)
admin.site.register(Category)
