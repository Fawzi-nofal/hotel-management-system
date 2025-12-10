from guest_cli_commands.base_command import GuestCommand

class UpdateGuestCommand(GuestCommand):
    def __init__(self, guest_service):
        self.guest_service = guest_service

    def execute(self):
        guest_id = input("Guest ID: ")
        new_name = input("New full name (leave blank to keep current): ")
        new_phone = input("New phone (leave blank to keep current): ")
        try:
            self.guest_service.update_guest_info(
                guest_id,
                new_name or None,
                new_phone or None
            )
            print("Guest updated.")
        except Exception as e:
            print(f"Error: {e}")
