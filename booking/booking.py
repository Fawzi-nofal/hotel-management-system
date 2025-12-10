from datetime import datetime
from  calculate_total_cost import BookingCostCalculator

class Booking:
    """Class for managing a hotel room booking."""

    STATUS_OPTIONS = {"checked-in", "checked-out"}

    def __init__(self, booking_id, guest, room, check_in_date, check_out_date):
        """
        Initialize a new booking.

        Args:
            booking_id (str): Unique booking identifier.
            guest (Guest): Guest object.
            room (Room): Room object.
            check_in_date (str): Check-in date in YYYY-MM-DD format.
            check_out_date (str): Check-out date in YYYY-MM-DD format.

        Raises:
            ValueError: If check-in is in the past or check-out is before check-in.
        """
        self.booking_id = booking_id
        self.guest = guest
        self.room = room
        self.check_in_date = datetime.strptime(check_in_date, "%Y-%m-%d")
        self.check_out_date = datetime.strptime(check_out_date, "%Y-%m-%d")
        if self.check_in_date < datetime.today():
            raise ValueError("Check-in cannot be in the past.")
        if self.check_out_date <= self.check_in_date:
            raise ValueError("Check-out must be after check-in.")
        self.status = "confirmed" 
        self.is_paid = False
        self.total_cost = BookingCostCalculator.calculate_total_cost(self)
        self.cancellation_fee = 0.0

    def mark_as_paid(self):
        """Mark booking as paid."""
        self.is_paid = True

    def update_status(self, new_status):
        """Update booking status if valid."""
        if new_status not in Booking.STATUS_OPTIONS:
            raise Exception(f"Invalid status: {new_status}")
        if new_status == "checked-out" and not self.is_paid:
            raise Exception("Cannot check out unpaid booking.")
        self.status = new_status

    def __str__(self):
        """Return a formatted string with booking details."""
        base_info = (
            f"Booking ID: {self.booking_id}\n"
            f"Guest: {self.guest.full_name} (ID: {self.guest.guest_id})\n"
            f"Room: {self.room.number}\n"
            f"Type: {self.room.get_typeroom()}\n"
            f"Check-in: {self.check_in_date.date()}\n"
            f"Check-out: {self.check_out_date.date()}\n"
            f"Status: {self.status}\n"
            f"Paid: {'Yes' if self.is_paid else 'No'}\n"
            f"Total Cost: ${self.total_cost:.2f}"
        )
        if self.status.lower() == "cancelled":
            base_info += f"\nCancellation Fee: ${self.cancellation_fee:.2f}"
        return base_info
