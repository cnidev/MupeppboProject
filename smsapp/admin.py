from django.contrib import admin
from .models import Mutualist

@admin.register(Mutualist)
class Mutualist(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone_number"]
    list_filter = ["first_name", "last_name"]
    search_fields = ["first_name", "last_name", "phone_number"]
    ordering = ("last_name",)