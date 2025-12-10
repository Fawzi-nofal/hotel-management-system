import unittest

class TestBookingLogic(unittest.TestCase):
    def test_placeholder(self):
        self.assertTrue(True)

# File: test_booking.py
import unittest
from datetime import datetime, timedelta
from guest.guest import Regular
from room.room import Standard
from booking.booking import Booking

class TestBooking(unittest.TestCase):
    def setUp(self):
        guest = Regular("G001", "John Doe", "0500000000")
        room = Standard(101)
        check_in = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
        check_out = (datetime.today() + timedelta(days=3)).strftime("%Y-%m-%d")
        self.booking = Booking("B001", guest, room, check_in, check_out)

    def test_total_cost(self):
        expected = 190 * 2  # 2 nights, no discount for Regular
        self.assertEqual(self.booking.total_cost, expected)

    def test_status_update(self):
        self.booking.update_status("checked-in")
        self.assertEqual(self.booking.status, "checked-in")

    def test_payment_mark(self):
        self.booking.mark_as_paid()
        self.assertTrue(self.booking.is_paid)
