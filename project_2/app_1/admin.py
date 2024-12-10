from django.contrib import admin
from .models import articles

# Register your models here.
@admin.register(articles)
class AdminArticle(admin.ModelAdmin):
    list_display = ['id','Heading','Description']
    list_display_links = ['Heading']
