
import unittest
from guest.guest import Member

class TestMemberLoyalty(unittest.TestCase):
    def test_accumulate_points_under_5_nights(self):
        guest = Member("G001", "Test Guest", "0501234567")
        points = guest.accumulate_points(3)
        self.assertEqual(points, 3)

    def test_accumulate_points_over_5_nights(self):
        guest = Member("G002", "Test Guest", "0501234567")
        points = guest.accumulate_points(6)
        self.assertEqual(points, 16)  # 6 nights + 10 bonus

    def test_accumulate_points_multiple_bookings(self):
        guest = Member("G003", "Test Guest", "0501234567")
        guest.accumulate_points(2)
        guest.accumulate_points(4)
        self.assertEqual(guest.points, 6)
