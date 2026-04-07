from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/<slug:category_slug>/', views.gallery, name='gallery_by_category'),
    path('contact/', views.contact, name='contact'),

    # Custom Dashboard URLs
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/categories/', views.dashboard_categories, name='dashboard_categories'),
    path('dashboard/categories/add/', views.category_create, name='category_create'),
    path('dashboard/categories/<int:pk>/edit/', views.category_update, name='category_update'),
    path('dashboard/categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    path('dashboard/photos/', views.dashboard_photos, name='dashboard_photos'),
    path('dashboard/photos/add/', views.photo_create, name='photo_create'),
    path('dashboard/photos/<int:pk>/edit/', views.photo_update, name='photo_update'),
    path('dashboard/photos/<int:pk>/delete/', views.photo_delete, name='photo_delete'),
    path('dashboard/messages/', views.dashboard_messages, name='dashboard_messages'),
    path('dashboard/messages/<int:pk>/', views.message_detail, name='message_detail'),
    path('dashboard/messages/<int:pk>/delete/', views.message_delete, name='message_delete'),
]
