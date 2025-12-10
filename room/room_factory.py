from room.room import Standard, Deluxe, Suite

class RoomFactory:
    """Factory for creating room instances based on type."""

    MAP = {
        "standard": Standard,
        "deluxe": Deluxe,
        "suite": Suite
    }

    @staticmethod
    def create(room_type, number):
        """
        Create a room instance by type and number.

        Args:
            room_type (str): The type of room (e.g., "standard", "deluxe", "suite").
            number (str or int): The room number.

        Returns:
            Room: An instance of the requested room type.

        Raises:
            ValueError: If the room type is unknown.
        """
        cls = RoomFactory.MAP.get(room_type.lower())
        if not cls:
            raise ValueError(f"Unknown room type: {room_type}")
        return cls(str(number))
