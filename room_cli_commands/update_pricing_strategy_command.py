from room_cli_commands.base_command import Command
from room.room_strategy import (
    RegularSeasonStrategy,
    PeakSeasonStrategy,
    WinterDiscountStrategy
)

class UpdatePricingStrategyCommand(Command):
    def __init__(self, room_service):
        self.room_service = room_service

    def execute(self):
        print("Choose pricing season:")
        print("1. Regular")
        print("2. Summer (+50%)")
        print("3. Winter (-20%)")

        choice = input("Season: ")
        if choice == "1":
            strategy = RegularSeasonStrategy()
        elif choice == "2":
            strategy = PeakSeasonStrategy()
        elif choice == "3":
            strategy = WinterDiscountStrategy()
        else:
            print("Invalid choice.")
            return

        for room in self.room_service.list_all_rooms():
            room.price_strategy = strategy

        self.room_service.repository.save_rooms(self.room_service.rooms)
        print("All room pricing strategies updated successfully.")
