from guest_cli_commands.base_command import GuestCommand

class UpdateGuestTypeCommand(GuestCommand):
    def __init__(self, guest_service):
        self.guest_service = guest_service

    def execute(self):
        try:
            guest_id = input("Guest ID to update type: ")
            print("Choose new guest type:")
            print("1. Regular\n2. VIP\n3. Member")
            type_map = { "1": "Regular", "2": "VIP", "3": "Member" }
            choice = input("Type (1-3): ")
            new_type = type_map.get(choice)

            if not new_type:
                print("Invalid type selected.")
                return

            result = self.guest_service.update_guest_type(guest_id, new_type)
            print(result)

        except Exception as e:
            print(f"Error: {e}")
