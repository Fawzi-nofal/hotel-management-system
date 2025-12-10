import unittest
import os
from datetime import datetime, timedelta
from booking.booking_service import BookingService
from Data.booking_data import BookingRepository
from guest.guest import Regular
from room.room import Standard

class FakeGuestService:
    def __init__(self):
        self.guests = {"G001": Regular("G001", "Test Guest", "0500000000")}

    def guest_exists(self, guest_id):
        return guest_id in self.guests

    def find_guest_by_id(self, guest_id):
        return self.guests[guest_id]

class FakeRoomService:
    def __init__(self):
        self.rooms = {101: Standard(101)}
        self.rooms[101].status = "available"
        
        # Repository מדומה עם מתודת load_rooms
        class DummyRepo:
            def load_rooms(inner_self):
                return self.rooms

        self.repository = DummyRepo()

    def mark_room_as_occupied(self, room_number):
        if room_number not in self.rooms:
            raise Exception(f"Room {room_number} not found")
        self.rooms[room_number].status = "occupied"

    def mark_room_as_available(self, room_number):
        if room_number not in self.rooms:
            raise Exception(f"Room {room_number} not found")
        self.rooms[room_number].status = "available"

    def list_all_rooms(self):
        return list(self.rooms.values())

    def get_room(self, room_number):
        if room_number not in self.rooms:
            raise Exception(f"Room {room_number} not found")
        return self.rooms[room_number]


class TestBookingService(unittest.TestCase):
    def setUp(self):
        self.guest_service = FakeGuestService()
        self.room_service = FakeRoomService()
        self.repository = BookingRepository("test_bookings.json")
        self.booking_service = BookingService(self.guest_service, self.room_service, self.repository)
        # Ensure no prior bookings interfere
        self.booking_service.bookings = {}

    def test_create_booking_success(self):
        check_in = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
        check_out = (datetime.today() + timedelta(days=3)).strftime("%Y-%m-%d")
        booking = self.booking_service.create_booking("B001", "G001", "standard", check_in, check_out)
        self.assertEqual(booking.booking_id, "B001")
        self.assertEqual(booking.room.status, "occupied")  # Verify room is marked occupied

    def test_create_booking_no_available_room(self):
        # Mark the only room as occupied
        self.room_service.mark_room_as_occupied(101)
        check_in = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
        check_out = (datetime.today() + timedelta(days=3)).strftime("%Y-%m-%d")
        with self.assertRaises(Exception):
            self.booking_service.create_booking("B002", "G001", "standard", check_in, check_out)

    def test_cancel_booking(self):
        check_in = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
        check_out = (datetime.today() + timedelta(days=3)).strftime("%Y-%m-%d")
        self.booking_service.create_booking("B003", "G001", "standard", check_in, check_out)
        result = self.booking_service.cancel_booking("B003")
        self.assertIn("cancelled", result.lower())
        self.assertEqual(self.room_service.rooms[101].status, "available")  # Verify room is available

    def tearDown(self):
        if os.path.exists("test_bookings.json"):
            os.remove("test_bookings.json")