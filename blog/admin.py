from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Post


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ("title", "id", "body",)
