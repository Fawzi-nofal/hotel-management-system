from datetime import datetime

class ReportUtils:
    """Utility class for generating room and booking reports."""

    def __init__(self, room_service, booking_service):
        """Initialize with room and booking services."""
        self.room_service = room_service
        self.bookings = booking_service.bookings

    def view_all_rooms_status(self):
        """
        Return a list of all rooms and their current status.

        Returns:
            list: List of Room objects.
        """
        rooms = self.room_service.list_all_rooms()
        room_view = []
        for room in rooms:
            room_view.append(room)
        return room_view

    def view_occupancy_rate(self):
        """
        Print the current occupancy rate as a percentage.
        """
        rooms = self.room_service.list_all_rooms()
        total = len(rooms)
        occupied = len([r for r in rooms if r.status.lower() == "occupied"])
        rate = (occupied / total) * 100 if total > 0 else 0
        print(f"Occupancy Rate: {rate:.2f}%")

    def view_upcoming_bookings(self):
        """
        Return a list of strings representing all upcoming bookings from today onward.

        Returns:
        list of str: Formatted upcoming bookings, or a list with a message if none found.
        """
        today = datetime.today().date()
        upcoming = [
            b for b in self.bookings.values()
            if b.check_in_date.date() >= today and b.status != "cancelled"
        ]

        if not upcoming:
            return ["No upcoming bookings."]

        upcoming.sort(key=lambda b: b.check_in_date)

        result = []
        for b in upcoming:
            result.append(f"Booking ID: {b.booking_id}")
            result.append(f"Guest: {b.guest.full_name} (ID: {b.guest.guest_id})")
            result.append(f"Room: {b.room.number} - Type: {b.room.get_typeroom()}")
            result.append(f"Check-in: {b.check_in_date.date()} | Check-out: {b.check_out_date.date()}")
            result.append(f"Status: {b.status}")
            result.append(f"Paid: {'Yes' if b.is_paid else 'No'}")
            result.append("-" * 40)
        return result

