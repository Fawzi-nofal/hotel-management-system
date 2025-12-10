import unittest
from guest.guest_logic import GuestLogic
from guest.guest import Regular, VIP, Member

class FakeGuestService:
    def list_all_guests(self):
        return [
            Regular("G001", "Alice", "0501"),
            VIP("G002", "David", "0502"),
            Member("G003", "Sara", "0503")
        ]

class TestGuestLogic(unittest.TestCase):
    def setUp(self):
        self.logic = GuestLogic(FakeGuestService(), {})  # ← מוסיף booking_data ריק

    def test_get_all_members(self):
        members = self.logic.get_all_members()
        self.assertEqual(len(members), 1)
        self.assertEqual(members[0].full_name, "Sara")

