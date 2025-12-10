from booking_cli_commands.base_command import Command
from booking.booking_logic import BookingLogic

class SearchBookingByDateCommand(Command):
    def __init__(self, booking_service):
        self.booking_logic = BookingLogic(booking_service.bookings)

    def execute(self):
        date_str = input("Enter date to search bookings (YYYY-MM-DD): ")
        results = self.booking_logic.search_bookings_by_date(date_str)
        if results:
            for b in results:
                print(b)
        else:
            print("No bookings found for that date.")