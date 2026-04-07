import os
import django
import requests
from django.core.files import File
from io import BytesIO

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neptuneshotit_site.settings')
django.setup()

from portfolio.models import Category, Photo

def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BytesIO(response.content)
    return None

def seed_data():
    # Define categories
    categories_data = [
        {'name': 'Weddings', 'slug': 'weddings'},
        {'name': 'Portraits', 'slug': 'portraits'},
        {'name': 'Events', 'slug': 'events'},
        {'name': 'Nature', 'slug': 'nature'},
    ]

    # Sample images from Unsplash
    photos_data = [
        {'title': 'Romantic Sunset Wedding', 'category_slug': 'weddings', 'url': 'https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=800&q=80', 'desc': 'A beautiful sunset ceremony captured at the beach.'},
        {'title': 'Classic Studio Portrait', 'category_slug': 'portraits', 'url': 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=800&q=80', 'desc': 'A minimalist studio portrait focusing on expression.'},
        {'title': 'Corporate Gala Event', 'category_slug': 'events', 'url': 'https://images.unsplash.com/photo-1511795409834-ef04bbd61622?auto=format&fit=crop&w=800&q=80', 'desc': 'High-energy coverage of a prestigious corporate event.'},
        {'title': 'Misty Mountain Morning', 'category_slug': 'nature', 'url': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=800&q=80', 'desc': 'Early morning mist rolling over the mountain peaks.'},
        {'title': 'Elegant Bridal Session', 'category_slug': 'weddings', 'url': 'https://images.unsplash.com/photo-1511285560929-80b456fea0bc?auto=format&fit=crop&w=800&q=80', 'desc': 'Close-up detail of bridal preparation and elegance.'},
        {'title': 'Urban Street Photography', 'category_slug': 'portraits', 'url': 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=800&q=80', 'desc': 'Authentic street style portrait in the heart of the city.'},
        {'title': 'Music Festival Night', 'category_slug': 'events', 'url': 'https://images.unsplash.com/photo-1533174072545-7a4b6ad7a6c3?auto=format&fit=crop&w=800&q=80', 'desc': 'Vibrant lighting and crowd energy at an outdoor festival.'},
        {'title': 'Forest Stream Detail', 'category_slug': 'nature', 'url': 'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=800&q=80', 'desc': 'Long exposure capture of a tranquil forest stream.'},
    ]

    print("Seeding categories...")
    for cat_info in categories_data:
        category, created = Category.objects.get_or_create(name=cat_info['name'], slug=cat_info['slug'])
        if created:
            print(f"Created category: {category.name}")

    print("Seeding photos...")
    for photo_info in photos_data:
        category = Category.objects.get(slug=photo_info['category_slug'])
        image_content = download_image(photo_info['url'])
        
        if image_content:
            photo = Photo(
                title=photo_info['title'],
                category=category,
                description=photo_info['desc']
            )
            # Use the slug and a number as filename
            filename = f"{photo_info['category_slug']}_{photo_info['title'].lower().replace(' ', '_')}.jpg"
            photo.image.save(filename, File(image_content), save=True)
            print(f"Created photo: {photo.title}")
        else:
            print(f"Failed to download image for: {photo_info['title']}")

if __name__ == '__main__':
    seed_data()
    print("Seeding complete!")
