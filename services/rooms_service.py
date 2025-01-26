from rooms.models import Room


def register_rooms(room):

    Room.objects.create(
        name=room.name,
        capacity=room.capacity,
        location=room.location,
    )
