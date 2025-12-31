# Admin configuration file
# This file registers models with Django admin
# Django admin is a built-in interface for managing data

# Import admin module
# NECESSARY: Provides admin functionality
from django.contrib import admin

# Import our models
# These are the models we defined in models.py
# We need to import them to register them
from .models import BlogPost, Comment, Category

# This is a comment
# Another comment
# Comments everywhere!


# BlogPost admin configuration
# This customizes how BlogPost appears in admin
# NECESSARY: Decorator registers the model with admin
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """
    Admin configuration for BlogPost model
    Customizes the admin interface
    """
    
    # List display
    # NECESSARY: Columns to show in list view
    # These are the fields shown in the table
    list_display = [
        'title',  # Post title
        'author',  # Author name
        'is_published',  # Published status
        'view_count',  # Number of views
        'created_at',  # Creation date
        'updated_at',  # Last update date
    ]
    
    # List filter
    # NECESSARY: Adds filters in sidebar
    # Users can filter by these fields
    list_filter = [
        'is_published',  # Filter by published status
        'created_at',  # Filter by creation date
        'author',  # Filter by author
    ]
    
    # Search fields
    # NECESSARY: Enables search functionality
    # Users can search by these fields
    search_fields = [
        'title',  # Search in title
        'content',  # Search in content
        'author',  # Search in author
    ]
    
    # Prepopulated fields
    # Not used here, but useful for slug fields
    # Automatically fills based on another field
    # prepopulated_fields = {'slug': ('title',)}
    
    # Date hierarchy
    # NECESSARY: Adds date-based navigation
    # Shows dates at top of list
    date_hierarchy = 'created_at'
    
    # Ordering
    # Default ordering in admin
    # Minus sign means descending
    ordering = ['-created_at']  # Newest first
    
    # List editable
    # Fields that can be edited in list view
    # Without opening detail page
    list_editable = ['is_published']  # Can toggle published status
    
    # Readonly fields
    # Fields that can't be edited
    # Usually auto-generated fields
    readonly_fields = ['created_at', 'updated_at', 'view_count']
    
    # Fieldsets
    # NECESSARY: Organizes fields into sections
    # Makes admin form cleaner
    fieldsets = (
        # First section - Basic Info
        # None is the section title (no title in this case)
        (None, {
            'fields': ('title', 'author', 'content')
        }),
        
        # Second section - Status
        # This has a title
        ('Status', {
            'fields': ('is_published',)
        }),
        
        # Third section - Metadata
        # Collapsed by default
        ('Metadata', {
            'fields': ('created_at', 'updated_at', 'view_count'),
            'classes': ('collapse',),  # NECESSARY: Makes section collapsible
        }),
    )


# Comment admin configuration
# Similar to BlogPost admin
# But with different fields
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin configuration for Comment model
    """
    
    # List display
    # Columns in list view
    list_display = [
        'name',  # Commenter name
        'post',  # Related blog post
        'email',  # Commenter email
        'is_approved',  # Approval status
        'created_at',  # When posted
    ]
    
    # List filter
    # Sidebar filters
    list_filter = [
        'is_approved',  # Filter by approval
        'created_at',  # Filter by date
    ]
    
    # Search fields
    # Searchable fields
    search_fields = [
        'name',  # Search by name
        'email',  # Search by email
        'text',  # Search in comment text
    ]
    
    # Date hierarchy
    # Date navigation
    date_hierarchy = 'created_at'
    
    # Ordering
    # Default order
    ordering = ['-created_at']  # Newest first
    
    # List editable
    # Can approve/reject in list view
    list_editable = ['is_approved']
    
    # Readonly fields
    # Can't edit creation date
    readonly_fields = ['created_at']
    
    # Raw ID fields
    # NECESSARY: For ForeignKey fields with many options
    # Shows ID input instead of dropdown
    # Better performance with many posts
    # raw_id_fields = ['post']


# Category admin configuration
# Simpler than the others
# Fewer fields to configure
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for Category model
    """
    
    # List display
    # Show name and slug
    list_display = [
        'name',  # Category name
        'slug',  # URL slug
    ]
    
    # Search fields
    # Search by name
    search_fields = ['name']
    
    # Prepopulated fields
    # NECESSARY: Auto-generate slug from name
    # Type name, slug fills automatically
    prepopulated_fields = {
        'slug': ('name',)  # Slug based on name
    }
    
    # Ordering
    # Alphabetical order
    ordering = ['name']


# Alternative registration method
# You can also register without decorator
# Like this:
# admin.site.register(BlogPost, BlogPostAdmin)
# admin.site.register(Comment, CommentAdmin)
# admin.site.register(Category, CategoryAdmin)

# But decorator is cleaner
# And more Pythonic
# So we used that instead

# You can also register without custom admin class
# Like this:
# admin.site.register(BlogPost)
# This uses default admin configuration
# But custom configuration is better
# More control over the interface

# End of admin file
# Now you can manage your models in Django admin
# Just create a superuser and login
# python manage.py createsuperuser
