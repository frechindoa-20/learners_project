from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'date_of_birth', 'phone')
    search_fields = ('last_name', 'first_name', 'email')
    list_filter = ('date_of_birth',)
    ordering = ('last_name', 'first_name')
    fieldsets = (
        ('Informations personnelles', {
            'fields': ('first_name', 'last_name', 'date_of_birth')
        }),
        ('Coordonnées', {
            'fields': ('email', 'phone', 'address')
        }),
    )
