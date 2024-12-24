from django.core.management.base import BaseCommand
from main.models import Room

class Command(BaseCommand):
    help = 'Generate rooms for the hotel'

    def handle(self, *args, **kwargs):
        Room.objects.all().delete()  # Удаляем существующие комнаты, если нужно
        for floor in range(1, 12):  # 11 этажей
            for number in range(1, 16):  # 15 номеров на каждом этаже
                room_number = floor * 100 + number  # Формат: 101, 102, ..., 111, ..., 1511
                room_type = (
                    'standard' if floor < 4 else
                    'comfort' if floor < 8 else
                    'lux'
                )
                Room.objects.create(
                    number=room_number,
                    floor=floor,
                    room_type=room_type,
                    price=1000 + floor * 100  # Пример цены
                )
        self.stdout.write(self.style.SUCCESS('Rooms generated successfully!'))
