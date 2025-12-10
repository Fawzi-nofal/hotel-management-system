from room_cli_commands.base_command import Command

class RemoveRoomCommand(Command):
    def __init__(self, room_service):
        self.room_service = room_service

    def execute(self):
        try:
            number = int(input("Room number to remove: "))
            print(self.room_service.remove_room(number))
        except Exception as e:
            print(f"Error: {e}")
