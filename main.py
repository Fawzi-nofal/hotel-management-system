from guest.guest_service import GuestService
from room.room_service import RoomService
from booking.booking_service import BookingService

from all_cli.guest_cli import GuestCLI
from all_cli.room_cli import RoomCLI
from all_cli.booking_cli import BookingCLI
from all_cli.manager_cli import ManagerCLI  

class HotelCLI:
    def __init__(self):
        self.guest_service = GuestService()
        self.room_service = RoomService()
        self.booking_service = BookingService(self.guest_service, self.room_service)

        self.guest_cli = GuestCLI(self.guest_service, self.booking_service)
        self.room_cli = RoomCLI(self.room_service)
        self.booking_cli = BookingCLI(self.booking_service)
        self.manager_cli = ManagerCLI(self.room_service, self.booking_service)  

    def run(self):
        while True:
            print("\n=== Hotel Management System ===")
            print("1. Room management ")
            print("2. Guest management")
            print("3. Booking management")
            print("4. Manager management")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "2":
                self.guest_cli.run()

            elif choice == "1":
                self.room_cli.run()

            elif choice == "3":
                self.booking_cli.run()

            elif choice == "4":
                self.manager_cli.run()

            elif choice == "5":
                print("Exiting Hotel Management System. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    HotelCLI().run()
