import unittest
from guest.guest_service import GuestService

class TestGuestService(unittest.TestCase):
    def setUp(self):
        self.service = GuestService()
        self.service.guests = {} 

    def test_add_guest(self):
        self.service.add_guest("regular", "G001", "John", "0500000000")
        guest = self.service.guests["G001"]
        self.assertEqual(guest.full_name, "John")
        self.assertEqual(guest.phone, "0500000000")
        self.assertEqual(guest.__class__.__name__, "Regular")


    def test_remove_guest(self):
        self.service.add_guest("vip", "G002", "Dana", "0500000001")
        result = self.service.remove_guest("G002")
        self.assertIn("successfully removed", result)

    def test_update_guest_info(self):
        self.service.add_guest("member", "G003", "Ori", "0500000002")
        msg = self.service.update_guest_info("G003", new_full_name="Oren")
        self.assertIn("updated successfully", msg)

    def test_update_guest_type(self):
        self.service.add_guest("regular", "G004", "Lior", "0500000003")
        result = self.service.update_guest_type("G004", "member")
        self.assertIn("member", result)
