from room_cli_commands.base_command import Command

class ListAvailableRoomsCommand(Command):
    def __init__(self, room_service):
        self.room_service = room_service

    def execute(self):
        available_rooms = [r for r in self.room_service.list_all_rooms() if r.status == "available"]
        if available_rooms:
            for room in available_rooms:
                print(room)
                print("----------")
        else:
            print("No available rooms found.")
