from datetime import datetime

class BookingLogic:
    """Logic class for searching and analyzing bookings."""

    def __init__(self, booking_data):
        """Initialize with existing booking data."""
        self.bookings = booking_data

    def get_guest_booking_history(self, guest_id):
        """
        Return all bookings for a given guest ID.

        Args:
            guest_id (str): The guest's unique identifier.

        Returns:
            list: List of Booking objects.
        """
        result = []
        for booking in self.bookings.values():
            if booking.guest.guest_id == guest_id:
                result.append(booking)
        return result

    def search_bookings_by_date(self, date_str):
        """
        Return bookings active on a specific date.

        Args:
            date_str (str): Date in 'YYYY-MM-DD' format.

        Returns:
            list: List of Booking objects active on that date.
        """
        target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        result = []
        for booking in self.bookings.values():
            if booking.check_in_date.date() <= target_date <= booking.check_out_date.date():
                result.append(booking)
        return result

    def search_bookings_by_guest(self, guest_name_or_id):
        """
        Search bookings by guest name or ID.

        Args:
            guest_name_or_id (str): Guest's full name or ID (partial match allowed).

        Returns:
            list: List of matching Booking objects.
        """
        target = guest_name_or_id.lower()
        result = []
        for booking in self.bookings.values():
            full_name = booking.guest.full_name.lower()
            guest_id = str(booking.guest.guest_id).lower()
            if target in full_name or target in guest_id:
                result.append(booking)
        return result
