from django.contrib import admin
from .models import Reservation
# Register your models here.


class ReserveAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'phone', 'date', 'time', 'number')
    list_display = ('name', 'email', 'phone', 'date', 'time')
    ordering = ('date', 'time')
    list_filter = ('date', 'number')


admin.site.register(Reservation, ReserveAdmin)
