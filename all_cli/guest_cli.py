from guest_cli_commands.add_guest_command import AddGuestCommand
from guest_cli_commands.list_guests_command import ListGuestsCommand
from guest_cli_commands.remove_guest_command import RemoveGuestCommand
from guest_cli_commands.update_guest_command import UpdateGuestCommand
from guest_cli_commands.guest_history_command import GuestHistoryCommand
from guest_cli_commands.update_guest_type_command import UpdateGuestTypeCommand


class GuestCLI:
    def __init__(self, guest_service,booking_service):
        self.guest_service = guest_service
        self.booking_service = booking_service
        self.commands = {
            "1": AddGuestCommand(self.guest_service),
            "2": RemoveGuestCommand(self.guest_service),
            "3": UpdateGuestCommand(self.guest_service),
            "4": UpdateGuestTypeCommand(self.guest_service),
            "5": ListGuestsCommand(self.guest_service),
            "6": GuestHistoryCommand(self.guest_service),
        }

    def run(self):
        while True:
            print("\n--- Guest Menu ---")
            print("1. Add guest")
            print("2. Remove guest")
            print("3. Update guest details")
            print("4. Update guest type")
            print("5. List guests")
            print("6. View guest booking history")
            print("7. Return to main menu")

            choice = input("Choose an option: ")
            if choice == "7":
                print("Returning to main menu.")
                break

            command = self.commands.get(choice)
            if command:
                command.execute()
            else:
                print("Invalid choice.")
