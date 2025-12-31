from django.contrib import admin
from .models import BlogPost, Comment, Category

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """Admin configuration for the BlogPost model."""
    list_display = [
        'title', 'author', 'is_published', 'view_count', 'created_at', 'updated_at'
    ]
    list_filter = ['is_published', 'created_at', 'author']
    search_fields = ['title', 'content', 'author']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    list_editable = ['is_published']
    readonly_fields = ['created_at', 'updated_at', 'view_count']
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'content')
        }),
        ('Status', {
            'fields': ('is_published',)
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at', 'view_count'),
            'classes': ('collapse',),
        }),
    )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin configuration for the Comment model."""
    list_display = ['name', 'post', 'email', 'is_approved', 'created_at']
    list_filter = ['is_approved', 'created_at']
    search_fields = ['name', 'email', 'text']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    list_editable = ['is_approved']
    readonly_fields = ['created_at']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin configuration for the Category model."""
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']
