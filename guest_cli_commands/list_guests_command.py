from guest_cli_commands.base_command import GuestCommand

class ListGuestsCommand(GuestCommand):
    def __init__(self, guest_service):
        self.guest_service = guest_service

    def execute(self):
        guests = self.guest_service.list_all_guests()
        if guests:
            for guest in guests:
                print(guest)
                print("---------")
        else:
            print("No guests found.")
