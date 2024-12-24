from django.db import models
from django.utils.translation import gettext_lazy as _

class RoomType(models.TextChoices):
    STANDARD = 'standard', _('Standard')
    COMFORT = 'comfort', _('Comfort')
    LUXURY = 'luxury', _('Luxury')

class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)  # Уникальный номер комнаты
    room_type = models.CharField(max_length=10, choices=RoomType.choices)  # Тип комнаты
    is_available = models.BooleanField(default=True)  # Доступность номера

    def __str__(self):
        return f"{self.room_number} ({self.get_room_type_display()})"

class Guest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")  # Связь с номером
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name="bookings")  # Связь с гостем
    check_in_date = models.DateField()  # Дата заселения
    check_out_date = models.DateField()  # Дата выселения
    created_at = models.DateTimeField(auto_now_add=True)  # Время создания брони

    def __str__(self):
        return f"Booking: {self.guest} in Room {self.room} ({self.check_in_date} - {self.check_out_date})"
