from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Room, Booking, Guest, RoomType
from datetime import datetime


def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def spa(request):
    return render(request, 'main/spa.html')

def attractions(request):
    return render(request, 'main/attractions.html')

def room_list_view(request):
    room_types = [
        {'type': RoomType.STANDARD, 'name': 'Standard', 'image': 'https://d1pe873sdaunfo.cloudfront.net/www.thechediandermatt.com-1165907230/cms/cache/v2/64413d46c601d.jpg/1920x1080/fit/80/2a795f95e488a7b89c95ab51beac2f35.jpg'},
        {'type': RoomType.COMFORT, 'name': 'Comfort', 'image': 'https://d1pe873sdaunfo.cloudfront.net/www.thechediandermatt.com-1165907230/cms/cache/v2/64413d4901767.jpg/768x553/fit;fp:47,50/80/2fb2084b4df4188b373dd4ab7d1081df.jpg'},
        {'type': RoomType.LUXURY, 'name': 'Luxury', 'image': 'https://d1pe873sdaunfo.cloudfront.net/www.thechediandermatt.com-1165907230/cms/cache/v2/64413d64e1000.jpg/1920x1080/fit/80/fbc019ca99236f837028e5fc9b094c23.jpg'},
    ]
    return render(request, 'main/room_list.html', {'room_types': room_types})



from django.shortcuts import render, redirect
from .models import Room, Booking, Guest, RoomType
from datetime import datetime

def booking_view(request):
    if request.method == 'POST':
        # Получение данных из POST-запроса
        room_type = request.POST.get('room_type')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        check_in_date = request.POST.get('check_in_date')
        check_out_date = request.POST.get('check_out_date')

        # Проверка заполненности данных
        if not (room_type and first_name and last_name and email and check_in_date and check_out_date):
            return render(request, 'main/error.html', {
                'error_message': 'All fields are required. Please fill out the form completely.'
            })

        # Проверка валидности дат
        try:
            check_in_date = datetime.strptime(check_in_date, '%Y-%m-%d').date()
            check_out_date = datetime.strptime(check_out_date, '%Y-%m-%d').date()
            if check_in_date >= check_out_date:
                return render(request, 'main/error.html', {
                    'error_message': 'Check-out date must be later than check-in date.'
                })
        except ValueError:
            return render(request, 'main/error.html', {
                'error_message': 'Invalid date format. Please use YYYY-MM-DD.'
            })

        # Проверка допустимой категории номера
        if room_type not in dict(RoomType.choices):
            return render(request, 'main/error.html', {
                'error_message': 'Invalid room type selected.'
            })

        # Поиск доступного номера
        available_room = Room.objects.filter(
            room_type=room_type
        ).exclude(
            bookings__check_out_date__gt=check_in_date,
            bookings__check_in_date__lt=check_out_date
        ).first()

        if not available_room:
            return render(request, 'main/error.html', {
                'error_message': 'No available rooms in the selected category for the given dates.'
            })

        # Создание гостя
        guest = Guest.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone
        )

        # Создание бронирования
        booking = Booking.objects.create(
            room=available_room,
            guest=guest,
            check_in_date=check_in_date,
            check_out_date=check_out_date
        )

        # Перенаправление на страницу успеха
        return redirect('booking_success')

    # Если GET-запрос, перенаправить на список номеров
    return redirect('room_list')

def booking_success(request):
    return render(request, 'main/booking_success.html')
def info(request):
    return render(request, 'main/info.html')
