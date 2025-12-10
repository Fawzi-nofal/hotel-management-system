from booking_cli_commands.base_command import Command

class ListBookingsCommand(Command):
    def __init__(self, booking_service):
        self.booking_service = booking_service

    def execute(self):
        bookings = self.booking_service.list_all_bookings()
        for b in bookings:
            print(b)
            print("----------")
