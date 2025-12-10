class GuestLogic:
    """Handles logic related to guests, like filtering and booking history."""

    def __init__(self, guest_service, booking_data):
        """Initialize with guest service and booking data."""
        self.guest_service = guest_service
        self.booking_data = booking_data

    def get_all_by_type(self, guest_type):
        """
        Return a list of all guests matching the given type.

        The type check is case-insensitive.
        """
        lst_type_guest = []
        all_guests = self.guest_service.list_all_guests()
        for guest in all_guests:
            if guest.type_guest().lower() == guest_type.lower():
                lst_type_guest.append(guest)
        return lst_type_guest

    def view_guest_booking_history(self, guest_id):
        """
        Return the booking history for a specific guest.

        Raises an error if the guest does not exist.
        """
        if not self.guest_service.guest_exists(guest_id):
            raise Exception(f"Guest with ID {guest_id} not found.")
        history = []
        for booking in self.booking_data.values():
            if booking.guest_id == guest_id:
                history.append(booking)
        return history
