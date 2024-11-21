from django.contrib import admin
from .models import One

@admin.register(One)
class OneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'timestamp', 'created_at', 'updated_at')
