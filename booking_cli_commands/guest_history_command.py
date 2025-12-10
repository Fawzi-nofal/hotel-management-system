from booking_cli_commands.base_command import Command
from booking.booking_logic import BookingLogic

class GuestHistoryCommand(Command):
    def __init__(self, booking_service):
        self.booking_logic = BookingLogic(booking_service.bookings)

    def execute(self):
        guest_id = input("Enter guest ID: ")
        history = self.booking_logic.get_guest_booking_history(guest_id)
        if history:
            for b in history:
                print(b)
                print("---------")
        else:
            print("No booking history for that guest.")