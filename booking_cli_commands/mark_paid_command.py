from booking_cli_commands.base_command import Command

class MarkPaidCommand(Command):
    def __init__(self, booking_service):
        self.booking_service = booking_service

    def execute(self):
        booking_id = input("Enter booking ID to mark as paid: ")
        try:
            result = self.booking_service.mark_booking_as_paid(booking_id)
            print(result)
        except Exception as e:
            print(e)
