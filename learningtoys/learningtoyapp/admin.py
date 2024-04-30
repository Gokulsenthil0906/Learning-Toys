from django.contrib import admin
from .models import contact

# admin.site.register(contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone', 'subject', 'message')
    search_fields = ('email','phone')

admin.site.register(contact,ContactAdmin)