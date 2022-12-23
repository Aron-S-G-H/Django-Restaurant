from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Food, Comment
# Register your models here.


class FoodAdmin(admin.ModelAdmin):
    readonly_fields = ('date', 'update_at', 'slug')
    list_display = ('name', 'food_type', 'price', 'situation', 'status')
    list_filter = ('food_type', 'situation', 'status')
    search_fields = ('name',)


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('name', 'food', 'created_at', 'text')
    list_filter = ('food',)


admin.site.unregister(Group)
admin.site.register(Food, FoodAdmin)
admin.site.register(Comment, CommentAdmin)
