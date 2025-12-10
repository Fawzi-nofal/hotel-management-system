
import unittest
from booking.booking import Booking
from guest.guest import Regular
from room.room import Standard
from datetime import datetime, timedelta

class TestCancellationFee(unittest.TestCase):
    def test_cancellation_fee_applied(self):
        guest = Regular("G001", "Test Guest", "0501234567")
        room = Standard(101)
        check_in = datetime.today() + timedelta(days=5)
        check_out = check_in + timedelta(days=3)
        booking = Booking("B001", guest, room, check_in.strftime("%Y-%m-%d"), check_out.strftime("%Y-%m-%d"))
        booking.update_status("cancelled")
        fee = booking.calculate_cancellation_fee()
        self.assertGreater(fee, 0)
