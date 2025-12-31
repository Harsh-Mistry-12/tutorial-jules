from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    """Represents a blog post."""
    title = models.CharField(
        max_length=200,
        help_text="The title of the blog post"
    )
    content = models.TextField(
        help_text="The main content of the blog post"
    )
    author = models.CharField(
        max_length=100,
        default="Anonymous"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="When the post was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="When the post was last updated"
    )
    is_published = models.BooleanField(
        default=False,
        help_text="Whether the post is published"
    )
    view_count = models.IntegerField(
        default=0,
        help_text="Number of times the post was viewed"
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title

    def increment_views(self):
        """Increments the view count by 1."""
        self.view_count += 1
        self.save()

class Comment(models.Model):
    """Represents a comment on a blog post."""
    post = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
        related_name='comments',
        help_text="The blog post this comment is on"
    )
    name = models.CharField(
        max_length=100,
        help_text="Name of the commenter"
    )
    email = models.EmailField(
        help_text="Email of the commenter"
    )
    text = models.TextField(
        help_text="The comment text"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="When the comment was posted"
    )
    is_approved = models.BooleanField(
        default=False,
        help_text="Whether the comment is approved"
    )

    class Meta:
        ordering = ['created_at']
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"

class Category(models.Model):
    """Represents a category for blog posts."""
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Category name"
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        help_text="URL-friendly version of name"
    )
    description = models.TextField(
        blank=True,
        help_text="Category description"
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
