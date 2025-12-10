from datetime import datetime

class RoomLogic:
    """Handles room-related logic like availability and filtering."""

    def __init__(self, room_service):
        """Initialize with a room service instance."""
        self.room_service = room_service

    def check_available_rooms(self):
        """
        Returns a list of all rooms that are currently available.
        """
        available_rooms = []
        for room in self.room_service.list_all_rooms():
            if room.status == "available":
                available_rooms.append(room)
        return available_rooms

    def check_available_rooms_by_type(self, room_type):
        """
        Returns available rooms that match the given room type.
        The comparison is case-insensitive.
        """
        types_rooms = []
        for room in self.check_available_rooms():
            if room.get_typeroom().lower() == room_type.lower():
                types_rooms.append(room)
        return types_rooms

    def is_room_available(self, room_number, check_in, check_out, bookings):
        """
        Checks if a specific room is available for the given date range.
        Considers the room's status and existing bookings.
        """
        try:
            check_in_date = datetime.strptime(check_in, "%Y-%m-%d").date()
            check_out_date = datetime.strptime(check_out, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        room = self.room_service.get_room(room_number)
        if room.status != "available":
            return False

        for booking in bookings.values():
            room_booked_number = booking.room.number
            if room_booked_number == room_number:
                if check_in_date < booking.check_out_date.date() and check_out_date > booking.check_in_date.date():
                    return False
        return True

    def check_available_rooms_by_type_and_date(self, room_type, check_in, check_out, bookings):
        """
        Returns available rooms of a specific type that are also available
        for the given date range.
        """
        available = []
        for room in self.room_service.list_all_rooms():
            if room.get_typeroom().lower() == room_type.lower():
                if self.is_room_available(room.number, check_in, check_out, bookings):
                    available.append(room)
        return available
