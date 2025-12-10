import json
from room.room import Standard, Deluxe, Suite

ROOM_TYPE_CLASSES = {
    "standard": Standard,
    "deluxe": Deluxe,
    "suite": Suite  
}

class RoomRepository:
    """Handles saving and loading room data from a JSON file."""

    def __init__(self, filename="rooms.json"):
        """Initialize with the filename for room storage."""
        self.filename = filename

    def load_rooms(self):
        """
        Load room data from the JSON file.

        Returns:
            dict: Dictionary of room_number -> Room objects.

        Raises:
            ValueError: If room type is unknown.
        """
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                rooms = {}
                for room_data in data:
                    room_type = room_data["type"].lower()
                    cls = ROOM_TYPE_CLASSES.get(room_type)
                    if cls is None:
                        raise ValueError(f"Unknown room type: {room_type}")
                    room = cls(str(room_data["number"]), room_data.get("status", "available"))
                    rooms[room.number] = room
                return rooms
        except FileNotFoundError:
            return {}

    def save_rooms(self, rooms):
        """
        Save room data to the JSON file.

        Args:
            rooms (dict): Dictionary of Room objects.
        """
        data = []
        for room in rooms.values():
            data.append({
                "number": str(room.number),
                "type": room.get_typeroom(),
                "status": room.status,
                "price": room.get_price()
            })
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)
