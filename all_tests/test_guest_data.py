import unittest
import os
from guest.guest import Regular
from Data.guest_data import GuestRepository

class TestGuestRepository(unittest.TestCase):
    def setUp(self):
        self.repo = GuestRepository("test_guests.json")
        self.data = {
            "G001": Regular("G001", "Alice", "0501234567")
        }

    def test_save_and_load(self):
        self.repo.save_guests(self.data)
        guests = self.repo.load_guests()
        self.assertIn("G001", guests)

    def tearDown(self):
        if os.path.exists("test_guests.json"):
            os.remove("test_guests.json")
