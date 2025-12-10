import unittest
import os
from room.room import Standard, Deluxe
from Data.room_data import RoomRepository

print("Loading room_data from:", __import__('Data.room_data').__file__)

class TestRoomRepository(unittest.TestCase):
    def setUp(self):
        self.repo = RoomRepository("test_rooms.json")
        self.test_rooms = {101: Standard(101), 102: Deluxe(102)}

    def test_save_and_load(self):
        self.repo.save_rooms(self.test_rooms)
        loaded = self.repo.load_rooms()
        self.assertIn(101, loaded)
        self.assertEqual(loaded[101].get_price(), 190)
        self.assertIn(102, loaded)
        self.assertEqual(loaded[102].get_typeroom(), "Deluxe")

    def test_load_empty_file(self):
        if os.path.exists("test_rooms.json"):
            os.remove("test_rooms.json")
        loaded = self.repo.load_rooms()
        self.assertEqual(loaded, {})

    def test_load_invalid_json(self):
        with open("test_rooms.json", "w") as f:
            f.write("invalid json")
        with self.assertRaises(ValueError):
            self.repo.load_rooms()

    def tearDown(self):
        if os.path.exists("test_rooms.json"):
            os.remove("test_rooms.json")