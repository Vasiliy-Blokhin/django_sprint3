from django.contrib import admin

from .models import Category, Location, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'text',
        'category',
        'pub_date',
        'is_published'
    ]
    list_display_links = [
        'title',
        'text',
        'pub_date',
    ]
    search_fields = [
        'title',
        'text'
    ]
    list_filter = [
        'category',
        'is_published'
    ]
    list_editable = [
        'category',
        'is_published'
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
        'is_published'
    ]
    list_display_links = [
        'title',
        'description',
    ]
    search_fields = [
        'title',
        'description'
    ]
    list_filter = [
        'is_published'
    ]
    list_editable = [
        'is_published'
    ]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'is_published'
    ]
    list_filter = [
        'is_published'
    ]
    list_editable = [
        'is_published'
    ]
