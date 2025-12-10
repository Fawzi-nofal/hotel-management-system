from booking_cli_commands.base_command import Command
from booking.booking_logic import BookingLogic

class CreateBookingCommand(Command):
    def __init__(self, booking_service):
        self.booking_service = booking_service

    def execute(self):
        booking_id = input("Booking ID: ")
        guest_id = input("Guest ID: ")
        print("Room type:\n1 - Standard\n2 - Deluxe\n3 - Suite")
        room_type_code = int(input("Enter room type number (1/2/3): "))
        TYPE_ROOM = {1: "standard", 2: "deluxe", 3: "suite"}

        if room_type_code not in TYPE_ROOM:
            print("Invalid room type code.")
            return

        room_type = TYPE_ROOM[room_type_code]
        check_in = input("Check-in (YYYY-MM-DD): ")
        check_out = input("Check-out (YYYY-MM-DD): ")

        try:
            booking = self.booking_service.create_booking(
                booking_id, guest_id, room_type, check_in, check_out
            )
            pay_now = input("Would you like to pay now? (y/n): ").strip().lower()
            if pay_now == "y":
                result = self.booking_service.mark_booking_as_paid(booking_id)
                print(result)
            else:
                print("Booking created. Payment is still pending.")
            print("Booking created successfully:")
            print(booking)
        except Exception as e:
            print(e)