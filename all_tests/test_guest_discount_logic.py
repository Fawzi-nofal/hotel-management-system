
import unittest
from guest.guest import Regular, VIP, Member

class TestGuestDiscountLogic(unittest.TestCase):
    def test_regular_discount(self):
        guest = Regular("G001", "Test Guest", "050")
        self.assertEqual(guest.discount(10), 0.0)

    def test_vip_discount(self):
        guest = VIP("G002", "VIP Guest", "051")
        self.assertEqual(guest.discount(10), 0.3)

    def test_member_discount_under_100_points(self):
        guest = Member("G003", "Member Guest", "052")
        guest.points = 50
        self.assertEqual(guest.discount(10), 0.0)

    def test_member_discount_over_100_points(self):
        guest = Member("G004", "Loyal Member", "053")
        guest.points = 110
        self.assertEqual(guest.discount(10), 0.1)
