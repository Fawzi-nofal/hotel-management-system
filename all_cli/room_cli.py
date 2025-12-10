from room_cli_commands.add_room_command import AddRoomCommand
from room_cli_commands.list_rooms_command import ListRoomsCommand
from room_cli_commands.remove_room_command import RemoveRoomCommand
from room_cli_commands.update_status_command import UpdateStatusCommand
from room_cli_commands.list_available_rooms_command import ListAvailableRoomsCommand
from room_cli_commands.maintenance_command import MaintenanceCommand
from room_cli_commands.update_type_coomand import UpdateRoomTypeCommand
from room_cli_commands.update_pricing_strategy_command import UpdatePricingStrategyCommand

class RoomCLI:
    def __init__(self, room_service):
        self.room_service = room_service
        self.commands = {
            "1": AddRoomCommand(self.room_service),
            "2": RemoveRoomCommand(self.room_service),
            "3": UpdateStatusCommand(self.room_service),
            "4": UpdateRoomTypeCommand(self.room_service),
            "5": UpdatePricingStrategyCommand(self.room_service),
            "6": MaintenanceCommand(self.room_service),
            "7": ListRoomsCommand(self.room_service),
            "8": ListAvailableRoomsCommand(self.room_service),
        }

    def run(self):
        while True:
            print("\n--- Room Menu ---")
            print("1. Add room")
            print("2. Remove room")
            print("3. Update room status (available / occupied)")
            print("4. update type room")
            print("5. Update price")
            print("6. Maintenance mode (set/remove)")
            print("7. List all rooms")
            print("8. List available rooms only")
            print("9. Exit room menu")

            choice = input("Choose an option: ")
            if choice == "9":
                print("Exiting room menu.")
                break

            command = self.commands.get(choice)
            if command:
                command.execute()
            else:
                print("Invalid choice.")
