# my-pythonDjango1/users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Custom form for user registration to add styling and placeholders
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply Tailwind classes and placeholders to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'block w-full border border-gray-300 rounded-md shadow-sm p-3 focus:ring-indigo-500 focus:border-indigo-500 placeholder-gray-400 text-gray-700',
                'placeholder': field.label # Set placeholder to field's label
            })

# Custom form for user login to add styling and placeholders
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply Tailwind classes and placeholders to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'block w-full border border-gray-300 rounded-md shadow-sm p-3 focus:ring-indigo-500 focus:border-indigo-500 placeholder-gray-400 text-gray-700',
                'placeholder': field.label # Set placeholder to field's label
            })
