# myQuill/admin.py

from django.contrib import admin
from django.utils.html import format_html
# Import all models you want to register
from .models import Post, Category, Tag, PostImage, Comment, Reply, Like


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return ""
    preview.short_description = "Image Preview"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'category', 'slug')
    list_filter = ('category', 'tags', 'date', 'author')
    search_fields = ('title', 'body', 'author__username')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PostImageInline]


@admin.register(Comment) # Register the Comment model
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'post', 'date', 'approved_comment') # Use 'date' instead of 'created_at'
    list_filter = ('approved_comment', 'date', 'post__title') # Filter by approved status, date, and post title
    search_fields = ('author__username', 'body', 'post__title') # Search by author, body, or post title
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved_comment=True)
    approve_comments.short_description = "Approve selected comments"


@admin.register(Reply) # Register the Reply model
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'comment', 'date')
    list_filter = ('date', 'comment__post__title') # Filter by date and associated post title
    search_fields = ('author__username', 'body', 'comment__body')


@admin.register(Like) # Register the Like model
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'date')
    list_filter = ('date', 'post__title')
    search_fields = ('user__username', 'post__title')


# Register other models (if not using @admin.register)
admin.site.register(Category)
admin.site.register(Tag)
# PostImage is managed via inline, so no need to register separately
# admin.site.register(PostImage)
