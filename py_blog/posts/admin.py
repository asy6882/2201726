from typing import Any
from django.contrib import admin
from posts.models import Post, PostImage, Comment
from django.contrib.admin.widgets import AdminFileWidget
from django.db import models
from django.utils.safestring import SafeText, mark_safe





# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    
    
class InlineImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        if value and getattr(value, "url", None):
            html = mark_safe(f'<img src="{value.url}" height="150">') + html
        return html
    

import admin_thumbnails


@admin_thumbnails.thumbnail("photo")
class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "content",
    ]
    inlines = [CommentInline, PostImageInline,]
    
    
@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "photo",
    ]
    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "content",
    ]