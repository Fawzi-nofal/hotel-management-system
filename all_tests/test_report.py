import unittest
from unittest.mock import patch
from reports.reports_manager import ReportUtils

class DummyRoom:
    def __init__(self, number_room, status):
        self.number_room = number_room
        self.status = status

    def get_typeroom(self):
        return "Standard"

class DummyRoomService:
    def list_all_rooms(self):
        return [DummyRoom(101, "available"), DummyRoom(102, "occupied")]

class DummyBookingService:
    bookings = []

class TestReportUtils(unittest.TestCase):
    def setUp(self):
        self.room_service = DummyRoomService()
        self.booking_service = DummyBookingService()
        self.report_utils = ReportUtils(self.room_service, self.booking_service)

    def test_view_all_rooms_status(self):
        rooms = self.report_utils.view_all_rooms_status()
        self.assertEqual(len(rooms), 2)
        self.assertEqual(rooms[0].number_room, 101)
        self.assertEqual(rooms[0].get_typeroom(), "Standard")
        self.assertEqual(rooms[0].status, "available")


    def test_view_occupancy_rate_runs(self):
        try:
            self.report_utils.view_occupancy_rate()
        except Exception as e:
            self.fail(f"view_occupancy_rate raised Exception unexpectedly: {e}")

if __name__ == '__main__':
    unittest.main()
