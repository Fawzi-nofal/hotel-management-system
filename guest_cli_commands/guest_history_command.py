from guest_cli_commands.base_command import GuestCommand

class GuestHistoryCommand(GuestCommand):
    def __init__(self, guest_logic):
        self.guest_logic = guest_logic

    def execute(self):
        guest_id = input("Enter Guest ID to view booking history: ")
        try:
            history = self.guest_logic.view_guest_booking_history(guest_id)
            if history:
                for booking in history:
                    print(booking)
            else:
                print("No bookings found for this guest.")
        except Exception as e:
            print(f"Error: {e}")
