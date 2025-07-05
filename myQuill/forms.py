# myQuill/forms.py

from django import forms
# Import the Comment model along with other models
from .models import Post, PostImage, Tag, Category, Comment
from django.forms.models import inlineformset_factory
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())  # Rich text field
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline mb-4'})
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-checkbox h-5 w-5 text-indigo-600'}),
        required=False
    )

    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'banner', 'category', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline mb-4'}),
            'slug': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline mb-4'}),
            'banner': forms.ClearableFileInput(attrs={'class': 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none'})
            # CKEditorWidget for 'body' is already defined above, no need to redefine here
        }


class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none'})
        }

# Inline formset for PostImage related to Post
PostImageFormSet = inlineformset_factory(Post, PostImage, form=PostImageForm, extra=3, can_delete=True)


# --- UPDATED COMMENTFORM HERE ---
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # Only 'body' is needed as 'author' is automatically set to request.user
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline h-32 resize-none', 'placeholder': 'Your Comment'}),
        }
        labels = {
            'body': 'Your Comment',
        }
# This form is used to create or edit comments on posts.