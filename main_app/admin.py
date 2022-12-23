from django.contrib import admin
from .models import Gallery, HomeSlider, ContactUs
# Register your models here.


class ImgAdmin(admin.ModelAdmin):
    readonly_fields = ('update_at', 'date')
    ordering = ('date',)


class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'message')
    list_display = ('name', 'email', 'phone', 'created_at')
    ordering = ('-created_at',)


admin.site.register(HomeSlider, ImgAdmin)
admin.site.register(Gallery, ImgAdmin)
admin.site.register(ContactUs, ContactAdmin)
