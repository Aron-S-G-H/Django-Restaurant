from django.contrib import admin
from .models import Blog, Category, Tag, Comment


class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update')
    list_display = ('title', 'author', 'category', 'situation', 'created_at')
    ordering = ('created_at',)
    list_filter = ('author', 'category', 'situation')


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('name', 'blog', 'created_at', 'text')
    list_filter = ('blog',)


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', 'date')
    list_display = ('title', 'date')
    ordering = ('-date',)
    search_fields = ('title',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
