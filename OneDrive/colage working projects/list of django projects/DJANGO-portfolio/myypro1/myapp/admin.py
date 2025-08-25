# myapp/admin.py

from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message', 'timestamp')
