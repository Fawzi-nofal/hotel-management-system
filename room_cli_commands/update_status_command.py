from room_cli_commands.base_command import Command

class UpdateStatusCommand(Command):
    def __init__(self, room_service):
        self.room_service = room_service

    def execute(self):
        try:
            number = int(input("Room number to update status: "))
            NEW_UPDATE = {1: "available", 2: "occupied"}
            print("New status:\n1) available\n2) occupied")
            status = int(input("Choose: "))
            if status not in NEW_UPDATE:
                print("Invalid status choice.")
                return
            new_status = NEW_UPDATE[status]
            room = self.room_service.get_room(number)
            room.status = new_status
            self.room_service.repository.save_rooms(self.room_service.rooms)
            print(f"Room {number} status updated to '{new_status}'.")
        except Exception as e:
            print(f"Error: {e}")
