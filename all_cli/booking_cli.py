from booking_cli_commands.create_booking_command import CreateBookingCommand
from booking_cli_commands.list_bookings_command import ListBookingsCommand
from booking_cli_commands.cancel_booking_command import CancelBookingCommand
from booking_cli_commands.search_booking_by_date_command import SearchBookingByDateCommand
from booking_cli_commands.search_booking_by_guest_command import SearchBookingByGuestCommand
from booking_cli_commands.guest_history_command import GuestHistoryCommand
from booking_cli_commands.view_invoice_command import ViewInvoiceCommand
from booking_cli_commands.mark_paid_command import MarkPaidCommand
from booking_cli_commands.update_booking_command import UpdateBookingCommand
from booking_cli_commands.update_booking_status_command import UpdateBookingStatusCommand

class BookingCLI:
    def __init__(self, booking_service):
        self.commands = {
            "1": CreateBookingCommand(booking_service),
            "2": CancelBookingCommand(booking_service),
            "3": UpdateBookingCommand(booking_service),
            "4": UpdateBookingStatusCommand(booking_service),
            "5": ListBookingsCommand(booking_service),
            "6": SearchBookingByDateCommand(booking_service),
            "7": SearchBookingByGuestCommand(booking_service),
            "8": GuestHistoryCommand(booking_service),
            "9": ViewInvoiceCommand(booking_service),
            "10": MarkPaidCommand(booking_service),
        }

    def run(self):
        while True:
            print("\n--- Booking Menu ---")
            print("1. Create booking")
            print("2. Cancel booking")
            print("3. Update booking detils")
            print("4. update status booking")
            print("5. List all bookings")
            print("6. Search bookings by date")
            print("7. Search bookings by guest name or ID")
            print("8. Show guest booking history")
            print("9. View invoice by booking ID")
            print("10. Mark booking as paid")
            print("11. Exit to main menu")

            choice = input("Choose: ")
            if choice == "11":
                break

            command = self.commands.get(choice)
            if command:
                command.execute()
            else:
                print("Invalid choice.")
