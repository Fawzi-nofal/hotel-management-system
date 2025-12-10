import unittest
from room.room_logic import RoomLogic
from room.room import Standard, Deluxe

class FakeRoomService:
    def __init__(self):
        self.rooms = [Standard(301), Deluxe(302)]
        self.rooms[1].status = "occupied"

    def list_all_rooms(self):
        return self.rooms

class TestRoomLogic(unittest.TestCase):
    def setUp(self):
        self.logic = RoomLogic(FakeRoomService())

    def test_check_available_rooms(self):
        rooms = self.logic.check_available_rooms()
        self.assertEqual(len(rooms), 1)
        self.assertEqual(rooms[0].number, 301)

    def test_check_available_rooms_by_type(self):
        rooms = self.logic.check_available_rooms_by_type("standard")
        self.assertEqual(len(rooms), 1)
        self.assertEqual(rooms[0].get_typeroom(), "Standard")

    def test_check_available_rooms_by_type_no_match(self):
        rooms = self.logic.check_available_rooms_by_type("suite")
        self.assertEqual(len(rooms), 0)
