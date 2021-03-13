from django.contrib import admin
from .models import post

# Register your models here.

class postAdmin(admin.ModelAdmin):
	list_display = ['name','description','user_id']

admin.site.register(post)
