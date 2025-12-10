import json
from booking.booking import Booking
from guest.guest import Regular, VIP, Member
from room.room import Standard, Deluxe, Suite
from Data.guest_data import GuestRepository
from Data.room_data import RoomRepository

ROOM_TYPE_CLASSES = {
    "standard": Standard,
    "deluxe": Deluxe,
    "suite": Suite
}

GUEST_TYPE_CLASSES = {
    "regular": Regular,
    "vip": VIP,
    "member": Member
}

class BookingRepository:
    """Handles saving and loading bookings from a JSON file."""

    def __init__(self, filename="bookings.json"):
        self.filename = filename

    def save_bookings(self, bookings):
        """Save bookings to JSON file."""
        data = []
        for booking in bookings.values():
            booking_data = {
                "booking_id": booking.booking_id,
                "guest_name": booking.guest.full_name,
                "guest_id": booking.guest.guest_id,
                "room_number": booking.room.number,
                "room_type": booking.room.get_typeroom(),
                "check_in": booking.check_in_date.strftime("%Y-%m-%d"),
                "check_out": booking.check_out_date.strftime("%Y-%m-%d"),
                "status": booking.status,
                "is_paid": booking.is_paid
            }
            data.append(booking_data)

        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_bookings(self):
        """
        Load bookings from the JSON file.
        Returns a dictionary of Booking objects.
        """
        guest_repo = GuestRepository()
        guests = guest_repo.load_guests()

        room_repo = RoomRepository()
        rooms = room_repo.load_rooms()

        try:
            with open(self.filename, "r") as f:
                content = f.read()
                if not content.strip():
                    return {}

                raw_data = json.loads(content)
                bookings = {}

                for item in raw_data:
                    guest_id = str(item["guest_id"])
                    guest = guests.get(guest_id)
                    if not guest:
                        raise ValueError(f"Guest with ID {guest_id} not found.")

                    room_number = str(item["room_number"])
                    room = rooms.get(room_number)
                    if not room:
                        raise ValueError(f"Room number {room_number} not found.")

                    booking = Booking(
                        booking_id=item["booking_id"],
                        guest=guest,
                        room=room,
                        check_in_date=item["check_in"],
                        check_out_date=item["check_out"]
                    )

                    booking.status = item.get("status", "confirmed")
                    booking.is_paid = item.get("is_paid", False)

                    bookings[booking.booking_id] = booking

                return bookings

        except FileNotFoundError:
            return {}
