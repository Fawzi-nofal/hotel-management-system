import unittest
from room.room import Standard, Deluxe, Suite

class TestStandard(unittest.TestCase):
    def setUp(self):
        self.room = Standard(101)

    def test_price(self):
        self.assertEqual(self.room.get_price(), 190)

    def test_type(self):
        self.assertEqual(self.room.get_typeroom(), "Standard")

    def test_status(self):
        self.assertEqual(self.room.status, "available")

    def test_str(self):
        self.assertIn("Standard", str(self.room))
        self.assertIn("101", str(self.room))

class TestDeluxe(unittest.TestCase):
    def setUp(self):
        self.room = Deluxe(102)

    def test_price(self):
        self.assertEqual(self.room.get_price(), 250)

    def test_type(self):
        self.assertEqual(self.room.get_typeroom(), "Deluxe")

    def test_status(self):
        self.assertEqual(self.room.status, "available")

    def test_str(self):
        self.assertIn("Deluxe", str(self.room))
        self.assertIn("102", str(self.room))

class TestSuite(unittest.TestCase):
    def setUp(self):
        self.room = Suite(103)

    def test_price(self):
        self.assertEqual(self.room.get_price(), 480)

    def test_type(self):
        self.assertEqual(self.room.get_typeroom(), "Suite")

    def test_status(self):
        self.assertEqual(self.room.status, "available")

    def test_str(self):
        self.assertIn("Suite", str(self.room))
        self.assertIn("103", str(self.room))