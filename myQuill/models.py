# myQuill/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField
from PIL import Image # Import Pillow
from io import BytesIO # For in-memory image manipulation
from django.core.files.uploadedfile import InMemoryUploadedFile # To save modified image
import sys # <--- CORRECTED: Added import sys

# --- Core Content Models ---

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = RichTextField()
    slug = models.SlugField(unique=True, blank=True, max_length=100)
    date = models.DateTimeField(default=timezone.now)
    banner = models.ImageField(default='fallback.png', blank=True, upload_to='post_banners/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Auto-generate slug
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        # Image Optimization for Banner
        if self.banner:
            # Check if the banner has changed or if it's a new image
            # This prevents re-optimizing on every save if image hasn't changed
            if not self.pk or not Post.objects.get(pk=self.pk).banner == self.banner:
                output_size = (800, 450) # Max width, max height for banner
                img = Image.open(self.banner)
                img.thumbnail(output_size, Image.Resampling.LANCZOS) # Resize while maintaining aspect ratio

                # Save the optimized image to a BytesIO object
                output = BytesIO()
                # Use format based on original image or force JPEG for smaller size
                img_format = img.format if img.format else 'JPEG'
                img.save(output, format=img_format, quality=85) # Adjust quality as needed
                output.seek(0)

                # Replace the original ImageField content with the optimized one
                self.banner = InMemoryUploadedFile(
                    output,
                    'ImageField',
                    f"{self.banner.name.split('.')[0]}.{img_format.lower()}", # Use original name, new format
                    'image/jpeg', # Or image/png depending on format
                    sys.getsizeof(output),
                    None
                )
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('myQuill:post_detail', kwargs={'slug': self.slug})


class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='post_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Image for post: {self.post.title}"

    def save(self, *args, **kwargs):
        # Image Optimization for Gallery Images
        if self.image:
            if not self.pk or not PostImage.objects.get(pk=self.pk).image == self.image:
                output_size = (600, 600) # Max width, max height for gallery images
                img = Image.open(self.image)
                img.thumbnail(output_size, Image.Resampling.LANCZOS)

                output = BytesIO()
                img_format = img.format if img.format else 'JPEG'
                img.save(output, format=img_format, quality=80)
                output.seek(0)

                self.image = InMemoryUploadedFile(
                    output,
                    'ImageField',
                    f"{self.image.name.split('.')[0]}.{img_format.lower()}",
                    'image/jpeg',
                    sys.getsizeof(output),
                    None
                )
        super().save(*args, **kwargs)


# --- User Interaction Models ---

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    class Meta:
        ordering = ['date']
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

    def approve(self):
        self.approved_comment = True
        self.save()


class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Replies"
        ordering = ['date']

    def __str__(self):
        return f"Reply by {self.author.username} to comment ID {self.comment.id}"

class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"
