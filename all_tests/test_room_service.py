import unittest
from room.room_service import RoomService
from Data.room_data import RoomRepository

class FakeRepo(RoomRepository):
    def __init__(self):
        self._data = {}

    def load_rooms(self):
        return self._data

    def save_rooms(self, rooms):
        self._data = rooms

class TestRoomService(unittest.TestCase):
    def setUp(self):
        self.service = RoomService(repository=FakeRepo())

    def test_add_room(self):
        result = self.service.add_room(200, "standard")
        self.assertIn("added", result.lower())
        self.assertIn(200, self.service.rooms)
        self.assertEqual(self.service.rooms[200].get_typeroom(), "Standard")

    def test_add_room_duplicate(self):
        self.service.add_room(201, "standard")
        with self.assertRaises(Exception):
            self.service.add_room(201, "deluxe")

    def test_remove_room(self):
        self.service.add_room(202, "standard")
        result = self.service.remove_room(202)
        self.assertIn("removed", result.lower())
        self.assertNotIn(202, self.service.rooms)

    def test_remove_room_not_found(self):
        with self.assertRaises(Exception):
            self.service.remove_room(999)

    def test_mark_as_occupied(self):
        self.service.add_room(203, "deluxe")
        self.service.mark_room_as_occupied(203)
        room = self.service.get_room(203)
        self.assertEqual(room.status, "occupied")

    def test_mark_as_occupied_not_found(self):
        with self.assertRaises(Exception):
            self.service.mark_room_as_occupied(999)

    def test_mark_as_available(self):
        self.service.add_room(204, "deluxe")
        self.service.mark_room_as_occupied(204)
        self.service.mark_room_as_available(204)
        room = self.service.get_room(204)
        self.assertEqual(room.status, "available")

    def test_update_room_type(self):
        self.service.add_room(205, "standard")
        result = self.service.update_room_type(205, "suite")
        self.assertIn("Suite", result)
        self.assertEqual(self.service.rooms[205].get_typeroom(), "Suite")

    def test_update_room_type_not_found(self):
        with self.assertRaises(Exception):
            self.service.update_room_type(999, "suite")