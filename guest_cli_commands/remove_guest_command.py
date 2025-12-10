from guest_cli_commands.base_command import GuestCommand

class RemoveGuestCommand(GuestCommand):
    def __init__(self, guest_service):
        self.guest_service = guest_service

    def execute(self):
        guest_id = input("Guest ID to remove: ")
        try:
            print(self.guest_service.remove_guest(guest_id))
        except Exception as e:
            print(f"Error: {e}")
