from Data.invoices_data import InvoiceDataGenerator
from reports.reports_manager import ReportUtils
from invoices.invoice import Invoice

class ManagerCLI:
    def __init__(self, room_service, booking_service):
        self.room_service = room_service
        self.booking_service = booking_service        
        self.report_utils = ReportUtils(room_service, booking_service)

    def run(self):
        while True:
            print("\n--- Manager Menu ---")
            print("1. View all invoices")
            print("2. View room occupancy rate")
            print("3. View upcoming bookings")
            print("4. Exit to main menu")

            choice = input("Choose: ")

            if choice == "1":
                invoices = InvoiceDataGenerator.load_all_invoices()
                if not invoices:
                    print("No invoices found.")
                else:
                    for invoice in invoices:
                        print_invoice(invoice)

            elif choice == "2":
                self.report_utils.view_occupancy_rate()


            elif choice == "3":
                results = self.report_utils.view_upcoming_bookings()
                print("\n--- Upcoming Bookings ---")
                for line in results:
                    print(line)


            elif choice == "4":
                break

            else:
                print("Invalid choice. Try again.")
def print_invoice(invoice):
    print("\n--- Invoice ---")
    print(f"Booking ID: {invoice['booking_id']}")
    print(f"Guest: {invoice['guest_name']} (ID: {invoice['guest_id']})")
    print(f"Room: {invoice['room_number']} ({invoice['room_type']})")
    print(f"Check-in: {invoice['check_in']}")
    print(f"Check-out: {invoice['check_out']}")
    print(f"Nights: {invoice['nights']}")
    print(f"Price per Night: {invoice['price_per_night']}₪")
    print(f"Discount: {invoice['discount']}")
    print(f"Total Cost: {invoice['total_cost']}₪")
    print(f"Paid: {'Yes' if invoice['is_paid'] else 'No'}")
    print(f"Invoice Status: {invoice['invoice_status']}")
    if "cancellation_fee" in invoice:
        print(f"Cancellation Fee: {invoice['cancellation_fee']}₪")
    if "points" in invoice:
        print(f"Points: {invoice['points']}")