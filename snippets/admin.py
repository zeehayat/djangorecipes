from django.contrib import admin
from django import forms
from .models import Snippet

# Register your models here.



class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'created_at')
    list_filter = ('language', 'created_at')
    search_fields = ('title','code')

class Meta:
    model = Snippet
    fields = '__all__'
    help_texts ={
        'code': 'Enter your code snippet here'
    }

admin.site.register(Snippet)