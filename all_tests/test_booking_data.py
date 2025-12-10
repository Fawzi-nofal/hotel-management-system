import unittest
import os
from Data.booking_data import BookingRepository
from guest.guest import Regular
from room.room import Standard
from booking.booking import Booking
from datetime import datetime, timedelta

class TestBookingRepository(unittest.TestCase):
    def setUp(self):
        self.repo = BookingRepository("test_bookings.json")
        guest = Regular("G001", "John Doe", "0500000000")
        room = Standard(101)
        check_in = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
        check_out = (datetime.today() + timedelta(days=3)).strftime("%Y-%m-%d")
        self.booking = Booking("B001", guest, room, check_in, check_out)
        self.repo.save_bookings({"B001": self.booking})

    def test_load_bookings(self):
        data = self.repo.load_bookings()
        self.assertIn("B001", data)
        self.assertEqual(data["B001"].guest.full_name, "John Doe")

    def tearDown(self):
        if os.path.exists("test_bookings.json"):
            os.remove("test_bookings.json")