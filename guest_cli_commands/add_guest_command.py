from guest_cli_commands.base_command import GuestCommand

class AddGuestCommand(GuestCommand):
    def __init__(self, guest_service):
        self.guest_service = guest_service

    def execute(self):
        try:
            guest_id = input("Guest ID: ")
            full_name = input("Full name: ")
            phone = input("Phone: ")
            TYPE_GUEST = {1: "Regular", 2: "VIP", 3: "Member"}
            print("1: Regular\n2: VIP\n3: Member")
            type_code = int(input("Type: "))
            type_guest = TYPE_GUEST[type_code]
            self.guest_service.add_guest(type_guest, guest_id, full_name, phone)
            print("Guest added successfully.")
        except Exception as e:
            print(f"Error: {e}")
