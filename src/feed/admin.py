from django.contrib import admin
from .models import Article, Comment, HashTag
# Register your models here.
@admin.register(Article, Comment, HashTag)
class feedAdmin(admin.ModelAdmin):
    pass
