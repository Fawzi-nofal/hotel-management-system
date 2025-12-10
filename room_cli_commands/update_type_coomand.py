from room_cli_commands.base_command import Command

class UpdateRoomTypeCommand(Command):
    def __init__(self, room_service):
        self.room_service = room_service

    def execute(self):
        try:
            number = input("number room: ")  
            NEW_TYPE = {1: "standard", 2: "deluxe", 3: "suite"}
            print("type room :\n1) standard\n2) deluxe\n3) suite")
            type_choice = int(input("Choose: "))  
            if type_choice not in NEW_TYPE:
                print("Invalid room type choice")  
                return
            new_type = NEW_TYPE[type_choice]
            result = self.room_service.update_room_type(number, new_type)
            print(result)
        except Exception as e:
            print(f"Error: {e}")  