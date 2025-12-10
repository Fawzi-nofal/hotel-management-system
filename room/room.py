from abc import ABC, abstractmethod
from room.room_strategy import RegularSeasonStrategy


class Room(ABC):
    """Base class for a hotel room."""
    def __init__(self, number, status="available", price_strategy=None):
        """Initialize a room with number, status, and price strategy."""
        self.number = number
        self.status = status
        self.price_strategy = price_strategy or RegularSeasonStrategy()

    @abstractmethod
    def get_typeroom(self):
        """Return the room type."""
        pass
    
    @abstractmethod
    def base_price(self):
        """Return the base price of the room."""
        pass
    
    def get_price(self):
        """Calculate the room price using the strategy."""
        return self.price_strategy.calculate_price(self.base_price())
    
    def mark_as_occupied(self):
        """Mark the room as occupied."""
        self.status = "occupied"

    def mark_as_available(self):
        """Mark the room as available."""
        self.status = "available"

    def mark_as_maintenance(self):
        """Mark the room as under maintenance."""
        if self.status != "available":
            raise Exception("Room must be available to go into maintenance.")
        self.status = "maintenance"
        
    def mark_as_available_from_maintenance(self):
        """Mark the room as available from maintenance."""
        if self.status != "maintenance":
            raise Exception(f"Room is not in maintenance mode.")
        self.status = "available"
    
    @staticmethod
    def update_type(old_room, new_type_class):
        """Create a new room with a different type, keeping status and pricing strategy."""
        new_room = new_type_class(old_room.number)
        new_room.status = old_room.status
        new_room.price_strategy = old_room.price_strategy  
        return new_room
    
    def __str__(self):
        """Return a string representation of the room."""
        return (
            f"Room number: {self.number}\n"
            f"Type room: {self.get_typeroom()}\n"
            f"Price: {self.get_price()}$\n"
            f"Status: {self.status}"
        )


class Standard(Room):
    """A standard hotel room."""
    
    def base_price(self):
        """Return the base price of a Standard room."""
        return 190
        
    def get_typeroom(self):
        """Return the room type as Standard."""
        return "Standard"


class Deluxe(Room):
    """A deluxe hotel room."""
    
    def base_price(self):
        """Return the base price of a Deluxe room."""
        return 250

    def get_typeroom(self):
        """Return the room type as Deluxe."""
        return "Deluxe"


class Suite(Room):
    """A suite hotel room."""
    
    def base_price(self):
        """Return the base price of a Suite room."""
        return 480

    def get_typeroom(self):
        """Return the room type as Suite."""
        return "Suite"
    