from room_cli_commands.base_command import Command

class ListRoomsCommand(Command):
    def __init__(self, room_service):
        self.room_service = room_service

    def execute(self):
        rooms = self.room_service.list_all_rooms()
        if not rooms:
            print("No rooms found.")
        for room in rooms:
            print(room)
            print("---------")
