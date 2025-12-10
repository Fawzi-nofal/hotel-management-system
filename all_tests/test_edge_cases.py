
import unittest
from guest.guest import Regular
from room.room import Standard
from booking.booking import Booking
from datetime import datetime, timedelta

class TestEdgeCases(unittest.TestCase):
    def test_invalid_check_out_before_check_in(self):
        guest = Regular("G001", "Test Guest", "050")
        room = Standard(100)
        check_in = datetime.today()
        check_out = check_in - timedelta(days=1)
        with self.assertRaises(ValueError):
            Booking("B003", guest, room, check_in.strftime("%Y-%m-%d"), check_out.strftime("%Y-%m-%d"))
