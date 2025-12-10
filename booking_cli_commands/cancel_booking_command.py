from booking_cli_commands.base_command import Command

class CancelBookingCommand(Command):
    def __init__(self, booking_service):
        self.booking_service = booking_service

    def execute(self):
        booking_id = input("Booking ID to cancel: ")
        try:
            print(self.booking_service.cancel_booking(booking_id))
        except Exception as e:
            print(e)