from booking_cli_commands.base_command import Command

class UpdateBookingCommand(Command):
    def __init__(self, booking_service):
        self.booking_service = booking_service

    def execute(self):
        try:
            booking_id = input("Enter booking ID to update: ")

            new_check_in = input("Enter new check-in date (YYYY-MM-DD) or press Enter to keep current: ").strip()
            new_check_out = input("Enter new check-out date (YYYY-MM-DD) or press Enter to keep current: ").strip()

            change_room = input("Do you want to change room type? (yes/no): ").strip().lower()
            new_room_type = None
            if change_room == "yes":
                print("Room type:\n1 - Standard\n2 - Deluxe\n3 - Suite")
                room_type_code = int(input("Enter room type number (1/2/3): "))
                TYPE_ROOM = {1: "standard", 2: "deluxe", 3: "suite"}
                new_room_type = TYPE_ROOM.get(room_type_code)

            updated_booking = self.booking_service.update_booking_details(
                booking_id,
                new_check_in if new_check_in else None,
                new_check_out if new_check_out else None,
                new_room_type
            )

            print("Booking updated successfully!")
            print(updated_booking)

        except Exception as e:
            print(f"Error: {e}")
