from booking_cli_commands.base_command import Command

class UpdateBookingStatusCommand(Command):
    def __init__(self, booking_service):
        self.booking_service = booking_service

    def execute(self):
        try:
            booking_id = input("Enter booking ID: ").strip()

            status_options = {
                1: "checked-in",
                2: "checked-out"
            }

            print("Choose new status:")
            print("1: checked-in")
            print("2: checked-out")

            choice = int(input("Enter your choice (1/2): "))

            if choice not in status_options:
                print("Invalid choice.")
                return

            new_status = status_options[choice]
            message = self.booking_service.update_booking_status(booking_id, new_status)
            print(message)

        except ValueError:
            print("Please enter a number (1 or 2).")
        except Exception as e:
            print(f"Error: {e}")
