from room_cli_commands.base_command import Command

class MaintenanceCommand(Command):
    def __init__(self, room_service):
        self.room_service = room_service

    def execute(self):
        try:
            number = int(input("Room number: "))
            print("1. Set room as under maintenance")
            print("2. Remove room from maintenance")
            sub_choice = input("Choose: ")
            if sub_choice == "1":
                print(self.room_service.mark_room_as_maintenance(number))
            elif sub_choice == "2":
                print(self.room_service.mark_room_as_available_from_maintenance(number))
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")
