from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .models import Category, Photo, ContactMessage
from .forms import CategoryForm, PhotoForm, ContactForm

# Existing views...
def home(request):
    categories = Category.objects.all()
    recent_photos = Photo.objects.all().order_by('-created_at')[:8]
    return render(request, 'portfolio/home.html', {
        'categories': categories,
        'recent_photos': recent_photos
    })

def gallery(request, category_slug=None):
    category = None
    photos = Photo.objects.all()
    categories = Category.objects.all()
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        photos = photos.filter(category=category)
        
    return render(request, 'portfolio/gallery.html', {
        'category': category,
        'categories': categories,
        'photos': photos
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('portfolio:contact')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})

# Custom Admin Dashboard Views
@user_passes_test(lambda u: u.is_staff)
def dashboard(request):
    category_count = Category.objects.count()
    photo_count = Photo.objects.count()
    message_count = ContactMessage.objects.filter(is_read=False).count()
    recent_photos = Photo.objects.all().order_by('-created_at')[:5]
    recent_messages = ContactMessage.objects.all().order_by('-created_at')[:5]
    return render(request, 'portfolio/dashboard/index.html', {
        'category_count': category_count,
        'photo_count': photo_count,
        'message_count': message_count,
        'recent_photos': recent_photos,
        'recent_messages': recent_messages
    })

@user_passes_test(lambda u: u.is_staff)
def dashboard_categories(request):
    categories = Category.objects.all()
    return render(request, 'portfolio/dashboard/category_list.html', {'categories': categories})

@user_passes_test(lambda u: u.is_staff)
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio:dashboard_categories')
    else:
        form = CategoryForm()
    return render(request, 'portfolio/dashboard/category_form.html', {'form': form, 'title': 'Add Category'})

@user_passes_test(lambda u: u.is_staff)
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('portfolio:dashboard_categories')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'portfolio/dashboard/category_form.html', {'form': form, 'title': 'Edit Category'})

@user_passes_test(lambda u: u.is_staff)
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('portfolio:dashboard_categories')
    return render(request, 'portfolio/dashboard/confirm_delete.html', {'item': category, 'type': 'Category'})

@user_passes_test(lambda u: u.is_staff)
def dashboard_photos(request):
    photos = Photo.objects.all().order_by('-created_at')
    return render(request, 'portfolio/dashboard/photo_list.html', {'photos': photos})

@user_passes_test(lambda u: u.is_staff)
def photo_create(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio:dashboard_photos')
    else:
        form = PhotoForm()
    return render(request, 'portfolio/dashboard/photo_form.html', {'form': form, 'title': 'Add Photo'})

@user_passes_test(lambda u: u.is_staff)
def photo_update(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('portfolio:dashboard_photos')
    else:
        form = PhotoForm(instance=photo)
    return render(request, 'portfolio/dashboard/photo_form.html', {'form': form, 'title': 'Edit Photo'})

@user_passes_test(lambda u: u.is_staff)
def photo_delete(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == 'POST':
        photo.delete()
        return redirect('portfolio:dashboard_photos')
    return render(request, 'portfolio/dashboard/confirm_delete.html', {'item': photo, 'type': 'Photo'})

# Dashboard Messages Views
@user_passes_test(lambda u: u.is_staff)
def dashboard_messages(request):
    messages_list = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'portfolio/dashboard/message_list.html', {'messages_list': messages_list})

@user_passes_test(lambda u: u.is_staff)
def message_detail(request, pk):
    message = get_object_or_404(ContactMessage, pk=pk)
    if not message.is_read:
        message.is_read = True
        message.save()
    return render(request, 'portfolio/dashboard/message_detail.html', {'message': message})

@user_passes_test(lambda u: u.is_staff)
def message_delete(request, pk):
    message = get_object_or_404(ContactMessage, pk=pk)
    if request.method == 'POST':
        message.delete()
        return redirect('portfolio:dashboard_messages')
    return render(request, 'portfolio/dashboard/confirm_delete.html', {'item': message, 'type': 'Message'})
