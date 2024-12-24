from .models import Room, RoomType

def populate_rooms():
    room_types = [
        {'type': RoomType.STANDARD, 'prefix': 'S'},
        {'type': RoomType.COMFORT, 'prefix': 'C'},
        {'type': RoomType.LUXURY, 'prefix': 'L'},
    ]

    for room_type in room_types:
        for i in range(1, 11):  # Создать 10 номеров
            room_number = f"{room_type['prefix']}{i:02d}"  # Например, S01, S02...
            Room.objects.create(
                room_number=room_number,
                room_type=room_type['type'],
                is_available=True
            )
    print("Rooms have been populated successfully.")
