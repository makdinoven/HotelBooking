from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import booking_view

urlpatterns = [
    path('api/bookings/', booking_view, name='booking-view'),
    path('', views.home, name='home'),  # Главная страница
    path('about/', views.about, name='about'),  # Страница "О нас"
    path('services/', views.services, name='services'),  # Услуги отеля
    path('spa/', views.spa, name='spa'),  # Страница "Спа"
    path('attractions/', views.attractions, name='attractions'),  # Достопримечательности
    path('rooms/', views.room_list_view, name='room_list'),  # Страница со списком номеров
    path('booking_success/', views.booking_success, name='booking_success'),
    path('info/', views.info, name='info'),
]

# Для корректной обработки медиафайлов (используется для изображений и других медиа)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
