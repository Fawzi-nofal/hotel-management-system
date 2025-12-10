from booking_cli_commands.base_command import Command
from booking.booking_logic import BookingLogic

class SearchBookingByGuestCommand(Command):
    def __init__(self, booking_service):
        self.booking_logic = BookingLogic(booking_service.bookings)

    def execute(self):
        query = input("Enter guest name or ID to search: ")
        results = self.booking_logic.search_bookings_by_guest(query)
        if results:
            for b in results:
                print(b)
        else:
            print("No matching bookings found.")