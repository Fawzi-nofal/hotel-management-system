from room.room import Room
from Data.room_data import RoomRepository
from room.room_factory import RoomFactory

class RoomService:
    """Service class for managing hotel rooms."""

    def __init__(self, repository=None):
        """Initialize with repository and load rooms."""
        self.repository = repository or RoomRepository()
        self.rooms = self.repository.load_rooms()

    def add_room(self, room_number, type_room):
        """Add a new room by number and type."""
        room_number = str(room_number)
        self.room_not_exists(room_number)
        if type_room.lower() not in RoomFactory.MAP:
            raise ValueError(f"Room type '{type_room}' not found")
        new_room = RoomFactory.create(type_room, room_number)
        self.rooms[room_number] = new_room
        self.repository.save_rooms(self.rooms)
        return f"Room {room_number} added as {type_room}."

    def remove_room(self, room_number):
        """Remove a room if it is not occupied or maintenance."""
        room_number = str(room_number)
        self.room_exists(room_number)
        room = self.rooms[room_number]
        if room.status == "occupied" or room.status == "maintenance":
            raise Exception(f"Room {room_number} is currently occupied or under maintenance and cannot be removed.")
        del self.rooms[room_number]
        self.repository.save_rooms(self.rooms)
        return f"Room {room_number} removed."

    def update_room_type(self, room_number, new_type):
        """Update the room type."""
        room_number = str(room_number)
        if room_number not in self.rooms:
            raise Exception("Room not found!")
        if new_type.lower() not in RoomFactory.MAP:
            raise ValueError(f"Room type '{new_type}' not found")
        room = self.rooms[room_number]
        if room.status == "occupied" or room.status == "maintenance":
            raise Exception(f"Room {room_number} is currently occupied or under maintenance and cannot be update type.")
        current_room = self.rooms[room_number]
        new_room_class = RoomFactory.MAP[new_type.lower()]
        updated_room = Room.update_type(current_room, new_room_class)
        self.rooms[room_number] = updated_room
        self.repository.save_rooms(self.rooms)
        return f"Room {room_number} updated to {updated_room.get_typeroom()}."

    def mark_room_as_occupied(self, room_number):
        """Set room status to occupied."""
        room_number = str(room_number)
        room = self.get_room(room_number)
        room.mark_as_occupied()
        self.repository.save_rooms(self.rooms)

    def mark_room_as_available(self, room_number):
        """Set room status to available."""
        room_number = str(room_number)
        room = self.get_room(room_number)
        room.mark_as_available()
        self.repository.save_rooms(self.rooms)

    def mark_room_as_maintenance(self, room_number):
        """Set room status to maintenance."""
        room_number = str(room_number)
        room = self.get_room(room_number)
        room.mark_as_maintenance()
        self.repository.save_rooms(self.rooms)
        return f"Room {room_number} marked as under maintenance."

    def mark_room_as_available_from_maintenance(self, room_number):
        """Set room status to available from maintenance."""
        room_number = str(room_number)
        room = self.get_room(room_number)
        room.mark_as_available_from_maintenance()
        self.repository.save_rooms(self.rooms)
        return f"Room {room_number} is now available."

    def get_room(self, room_number):
        """Return room by number or raise error."""
        room_number = str(room_number)
        room = self.rooms.get(room_number)
        if not room:
            raise Exception(f"Room {room_number} not found.")
        return room

    def room_not_exists(self, room_number):
        """Raise error if room already exists."""
        room_number = str(room_number)
        if room_number in self.rooms:
            raise Exception(f"Room {room_number} already exists.")

    def room_exists(self, room_number):
        """Raise error if room does not exist."""
        room_number = str(room_number)
        if room_number not in self.rooms:
            raise Exception(f"Room {room_number} does not exist.")

    def list_all_rooms(self):
        """Return a list of all rooms."""
        return list(self.rooms.values())
