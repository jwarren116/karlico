from django.contrib import admin

from blog.models import BlogPost, Image, Category


class ImageInline(admin.StackedInline):
    model = Image
    extra = 1


class PostAdmin(admin.ModelAdmin):
    model = BlogPost
    inlines = [ImageInline]
    list_display = ('title', 'category', 'content', 'created', 'display')
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('category', 'slug')
    prepopulated_fields = {'slug': ('category',)}


admin.site.register(BlogPost, PostAdmin)
admin.site.register(Category, CategoryAdmin)
