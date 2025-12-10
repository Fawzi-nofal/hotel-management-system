from room_cli_commands.base_command import Command

class AddRoomCommand(Command):
    def __init__(self, room_service):
        self.room_service = room_service

    def execute(self):
        try:
            number = int(input("Room number: "))
            print("1: standard\n2: deluxe\n3: suite")
            room_type_code = int(input("Room type: "))
            ROOM_TYPE = {1: "standard", 2: "deluxe", 3: "suite"}
            room_type = ROOM_TYPE[room_type_code]
            print(self.room_service.add_room(number, room_type))
        except Exception as e:
            print(f"Error: {e}")
