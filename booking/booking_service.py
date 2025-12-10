from room.room_logic import RoomLogic
from booking.booking import Booking
from Data.booking_data import BookingRepository
from Data.invoices_data import InvoiceDataGenerator
from datetime import datetime
from booking_cancellation_fee import BookingCancellationCalculator

class BookingService:
    """Service class for managing bookings."""

    def __init__(self, guest_service, room_service, repository=None):
        """Initialize with services and load bookings."""
        self.repository = repository or BookingRepository()
        self.bookings = self.repository.load_bookings()  
        self.guest_service = guest_service
        self.room_service = room_service
        self.room_logic = RoomLogic(self.room_service)

    def create_booking(self, booking_id, guest_id, room_type, check_in, check_out):
        """
        Create a new booking if room is available.

        Args:
            booking_id (str): Booking identifier.
            guest_id (str): Guest identifier.
            room_type (str): Desired room type.
            check_in (str): Check-in date (YYYY-MM-DD).
            check_out (str): Check-out date (YYYY-MM-DD).

        Returns:
            Booking: The created booking object.
        """
        if booking_id in self.bookings:
            raise Exception("Booking ID already exists.")
        self.guest_service.guest_exists(guest_id)
        guest_obj = self.guest_service.find_guest_by_id(guest_id)
        available_rooms = self.room_logic.check_available_rooms_by_type_and_date(
            room_type, check_in, check_out, self.bookings
        )
        if not available_rooms:
            raise Exception("No available rooms of the requested type.")
        selected_room = available_rooms[0]
        self.room_service.mark_room_as_occupied(selected_room.number)
        booking = Booking(booking_id, guest_obj, selected_room, check_in, check_out)
        self.bookings[booking_id] = booking
        if hasattr(guest_obj, "accumulate_points"):
            nights = (booking.check_out_date - booking.check_in_date).days
            guest_obj.accumulate_points(nights)
            self.guest_service.repository.save_guests(self.guest_service.guests)
        self.repository.save_bookings(self.bookings)
        InvoiceDataGenerator.save_json_to_file(booking, invoice_status="issued")
        return booking

    def cancel_booking(self, booking_id):
        """
        Cancel a booking and apply cancellation fee.

        Args:
            booking_id (str): Booking identifier.

        Returns:
            str: Confirmation message with fee.
        """
        if booking_id not in self.bookings:
            raise Exception("Booking ID not found.")
        booking = self.bookings[booking_id]
        booking.update_status("cancelled")
        self.room_service.mark_room_as_available(booking.room.number)
        self.room_service.rooms = self.room_service.repository.load_rooms()
        cancellation_fee = BookingCancellationCalculator.calculate_cancellation_fee(booking)
        booking.cancellation_fee = cancellation_fee
        self.repository.save_bookings(self.bookings)
        InvoiceDataGenerator.save_json_to_file(booking, invoice_status="cancelled")
        return f"Booking {booking_id} has been cancelled. Cancellation fee: {cancellation_fee:.2f} $"

    

    def update_booking_details(self, booking_id, new_check_in=None, new_check_out=None, new_room_type=None):
        """
        Update booking dates and/or room type.

        Args:
        booking_id (str): Booking identifier.
        new_check_in (str): New check-in date (optional).
        new_check_out (str): New check-out date (optional).
        new_room_type (str): New room type to assign (optional).

        Returns:
        Booking: The updated booking object.
        """
        if booking_id not in self.bookings:
            raise Exception("Booking ID not found.")
        booking = self.bookings[booking_id]
        if new_check_in:
            new_check_in_date = datetime.strptime(new_check_in, "%Y-%m-%d")
            if new_check_in_date.date() < datetime.today().date():
                raise ValueError("Check-in date cannot be in the past.")
            booking.check_in_date = new_check_in_date
        if new_check_out:
            new_check_out_date = datetime.strptime(new_check_out, "%Y-%m-%d")
            if new_check_out_date <= booking.check_in_date:
                raise ValueError("Check-out must be after check-in.")
            booking.check_out_date = new_check_out_date

        check_in = booking.check_in_date.strftime("%Y-%m-%d")
        check_out = booking.check_out_date.strftime("%Y-%m-%d")

        if new_room_type:
            available_rooms = self.room_logic.check_available_rooms_by_type_and_date(
            new_room_type, check_in, check_out, self.bookings)
        
            if not available_rooms:
                raise Exception(f"No available rooms of type '{new_room_type}' for the given dates.")
            self.room_service.mark_room_as_available(booking.room.number)
            new_room = available_rooms[0]
            self.room_service.mark_room_as_occupied(new_room.number)
            booking.room = new_room
        else:
            for other_booking in self.bookings.values():
                if other_booking.booking_id == booking.booking_id:
                    continue  
                if other_booking.room.number == booking.room.number and other_booking.status != "cancelled":
                    if check_in < other_booking.check_out_date and check_out > other_booking.check_in_date:
                        raise Exception(f"Room {booking.room.number} is not available for the new dates.")

        booking.total_cost = booking.calculate_total_cost()    
        self.repository.save_bookings(self.bookings)
        InvoiceDataGenerator.save_json_to_file(booking)
        return booking


    def update_booking_status(self, booking_id, new_status):
        """
        Update the status of a booking.

        Args:
            booking_id (str): Booking identifier.
            new_status (str): New status ("checked-in", "checked-out", "cancelled").

        Returns:
            str: Confirmation message.
        """
        if booking_id not in self.bookings:
            raise Exception("Booking ID not found.")
        booking = self.bookings[booking_id]
        booking.update_status(new_status)
        self.repository.save_bookings(self.bookings)
        InvoiceDataGenerator.save_json_to_file(booking)
        return f"Status for booking {booking_id} updated to {new_status}."

    def mark_booking_as_paid(self, booking_id):
        """
        Mark a booking as paid.

        Args:
            booking_id (str): Booking identifier.

        Returns:
            str: Confirmation message.
        """
        if booking_id not in self.bookings:
            raise Exception("Booking ID not found.")
        booking = self.bookings[booking_id]
        booking.mark_as_paid()
        self.repository.save_bookings(self.bookings)
        InvoiceDataGenerator.save_json_to_file(booking, invoice_status="paid")
        return f"Booking {booking_id} marked as paid."

    def list_all_bookings(self):
        """Return a list of all bookings."""
        return list(self.bookings.values())
