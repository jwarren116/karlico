from django.contrib import admin

from blog.models import BlogPost, Image, Category, About, Link


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


class LinkInline(admin.StackedInline):
    model = Link
    extra = 2


class AboutAdmin(admin.ModelAdmin):
    model = About
    inlines = [LinkInline]

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else True


admin.site.register(BlogPost, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(About, AboutAdmin)
