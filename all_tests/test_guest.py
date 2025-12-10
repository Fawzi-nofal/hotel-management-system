import unittest
from guest.guest import Regular, VIP, Member

class TestRegularGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Regular("G001", "Alice", "0501234567")


    def test_type(self):
        self.assertEqual(self.guest.type_guest(), "Regular")


class TestVIPGuest(unittest.TestCase):
    def setUp(self):
        self.guest = VIP("G002", "David", "0509876543")

    def test_discount(self):
        self.assertEqual(self.guest.discount(5), 0.3)

    def test_type(self):
        self.assertEqual(self.guest.type_guest(), "VIP")


class TestMemberGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Member("G003", "Sara", "0521112222")

    def test_discount_levels(self):
        self.assertEqual(self.guest.accumulate_points(2), 2)     
        self.assertEqual(self.guest.accumulate_points(1), 3)     
        self.assertEqual(self.guest.accumulate_points(6), 19)    

    def test_points_accumulation(self):
        self.assertEqual(self.guest.accumulate_points(3), 3)  
        self.assertEqual(self.guest.accumulate_points(2), 5)   
        self.assertEqual(self.guest.accumulate_points(6), 21)  

