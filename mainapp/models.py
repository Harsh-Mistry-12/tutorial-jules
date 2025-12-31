# Models file
# This defines database models
# Models are Python classes that represent database tables

# Import models from Django
# NECESSARY: This is the base class for all models
from django.db import models

# Import timezone
# For datetime fields
from django.utils import timezone

# This is a comment
# Another comment
# Yet another comment


# Blog Post model
# This represents a blog post in the database
# Each instance is a row in the table
class BlogPost(models.Model):
    """
    Blog post model
    Stores blog post data in database
    """
    
    # Title field
    # NECESSARY: CharField for short text
    # max_length is required for CharField
    title = models.CharField(
        max_length=200,  # Maximum 200 characters
        help_text="The title of the blog post"  # Help text for admin
    )
    
    # Content field
    # TextField for long text
    # No max_length needed
    content = models.TextField(
        help_text="The main content of the blog post"
    )
    
    # Author field
    # CharField for author name
    # Could also be a ForeignKey to User model
    author = models.CharField(
        max_length=100,  # Maximum 100 characters
        default="Anonymous"  # Default value if not provided
    )
    
    # Created date
    # NECESSARY: auto_now_add sets timestamp when created
    # This is automatically set
    created_at = models.DateTimeField(
        auto_now_add=True,  # Set on creation
        help_text="When the post was created"
    )
    
    # Updated date
    # auto_now updates timestamp on every save
    # Different from auto_now_add
    updated_at = models.DateTimeField(
        auto_now=True,  # Update on every save
        help_text="When the post was last updated"
    )
    
    # Published status
    # Boolean field
    # True or False
    is_published = models.BooleanField(
        default=False,  # Not published by default
        help_text="Whether the post is published"
    )
    
    # View count
    # Integer field
    # Tracks how many times post was viewed
    view_count = models.IntegerField(
        default=0,  # Starts at 0
        help_text="Number of times the post was viewed"
    )
    
    # Meta class
    # NECESSARY: Defines metadata for the model
    class Meta:
        # Ordering
        # How to order query results
        # Minus sign means descending order
        ordering = ['-created_at']  # Newest first
        
        # Verbose name
        # Human-readable name
        verbose_name = "Blog Post"
        
        # Plural name
        # For admin interface
        verbose_name_plural = "Blog Posts"
    
    # String representation
    # NECESSARY: Defines how model appears as string
    # Used in admin and shell
    def __str__(self):
        # Return the title
        # This is what you see in admin
        return self.title
    
    # Custom method
    # Not a built-in Django method
    # We created this ourselves
    def increment_views(self):
        """
        Increment the view count
        Call this when post is viewed
        """
        # Increase view count by 1
        self.view_count += 1
        
        # Save to database
        # NECESSARY: Changes aren't saved automatically
        self.save()


# Comment model
# For comments on blog posts
# Related to BlogPost model
class Comment(models.Model):
    """
    Comment model
    Stores comments on blog posts
    """
    
    # Foreign key to BlogPost
    # NECESSARY: Links comment to a blog post
    # on_delete=CASCADE means delete comments when post is deleted
    post = models.ForeignKey(
        BlogPost,  # Related model
        on_delete=models.CASCADE,  # Delete comments if post deleted
        related_name='comments',  # Reverse relation name
        help_text="The blog post this comment is on"
    )
    
    # Commenter name
    # CharField for name
    name = models.CharField(
        max_length=100,  # Maximum 100 characters
        help_text="Name of the commenter"
    )
    
    # Email field
    # NECESSARY: EmailField validates email format
    # Not CharField
    email = models.EmailField(
        help_text="Email of the commenter"
    )
    
    # Comment text
    # TextField for the actual comment
    text = models.TextField(
        help_text="The comment text"
    )
    
    # Created date
    # When comment was posted
    created_at = models.DateTimeField(
        auto_now_add=True,  # Set automatically
        help_text="When the comment was posted"
    )
    
    # Approved status
    # For comment moderation
    # Admin can approve/reject comments
    is_approved = models.BooleanField(
        default=False,  # Not approved by default
        help_text="Whether the comment is approved"
    )
    
    # Meta class
    class Meta:
        # Ordering
        # Oldest first for comments
        ordering = ['created_at']  # No minus sign
        
        # Verbose names
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
    
    # String representation
    def __str__(self):
        # Return comment preview
        # First 50 characters
        return f"Comment by {self.name} on {self.post.title}"


# Category model
# For categorizing blog posts
# Simple model
class Category(models.Model):
    """
    Category model
    For organizing blog posts
    """
    
    # Category name
    # Unique means no duplicates
    name = models.CharField(
        max_length=100,  # Maximum 100 characters
        unique=True,  # NECESSARY: No duplicate categories
        help_text="Category name"
    )
    
    # Slug field
    # NECESSARY: URL-friendly version of name
    # Used in URLs
    slug = models.SlugField(
        max_length=100,  # Maximum 100 characters
        unique=True,  # Must be unique
        help_text="URL-friendly version of name"
    )
    
    # Description
    # Optional field
    # blank=True means it's optional
    description = models.TextField(
        blank=True,  # Optional
        help_text="Category description"
    )
    
    # Meta class
    class Meta:
        # Verbose names
        verbose_name = "Category"
        verbose_name_plural = "Categories"  # Correct plural
        
        # Ordering
        # Alphabetical order
        ordering = ['name']
    
    # String representation
    def __str__(self):
        # Return category name
        return self.name


# End of models file
# These models aren't used in the views yet
# But they're here for demonstration
# You can use them in Django admin
# Or create views to display them
