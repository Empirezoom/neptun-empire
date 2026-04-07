from django import forms
from .models import Category, Photo, ContactMessage

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full bg-zinc-900 border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-white/40'}),
            'slug': forms.TextInput(attrs={'class': 'w-full bg-zinc-900 border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-white/40'}),
        }

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image', 'category', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full bg-zinc-900 border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-white/40'}),
            'category': forms.Select(attrs={'class': 'w-full bg-zinc-900 border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-white/40'}),
            'description': forms.Textarea(attrs={'class': 'w-full bg-zinc-900 border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-white/40 h-32 resize-none'}),
            'image': forms.FileInput(attrs={'class': 'w-full bg-zinc-900 border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-white/40'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'autocomplete': 'name', 'aria-required': 'true', 'class': 'w-full bg-black/50 border border-white/10 rounded-xl px-6 py-4 text-white focus:outline-none focus:border-white/40 transition-all placeholder:text-gray-700'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'autocomplete': 'email', 'aria-required': 'true', 'class': 'w-full bg-black/50 border border-white/10 rounded-xl px-6 py-4 text-white focus:outline-none focus:border-white/40 transition-all placeholder:text-gray-700'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject', 'aria-required': 'true', 'class': 'w-full bg-black/50 border border-white/10 rounded-xl px-6 py-4 text-white focus:outline-none focus:border-white/40 transition-all placeholder:text-gray-700'}),
            'message': forms.Textarea(attrs={'placeholder': 'Tell us more about your project...', 'rows': 6, 'aria-required': 'true', 'class': 'w-full bg-black/50 border border-white/10 rounded-xl px-6 py-4 text-white focus:outline-none focus:border-white/40 transition-all placeholder:text-gray-700 resize-none'}),
        }
