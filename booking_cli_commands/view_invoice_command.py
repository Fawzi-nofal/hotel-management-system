from booking_cli_commands.base_command import Command
from Data.invoices_data import InvoiceDataGenerator

class ViewInvoiceCommand(Command):
    def __init__(self, booking_service):
        self.booking_service = booking_service

    def execute(self):
        booking_id = input("Enter booking ID to view invoice: ")
        invoices = InvoiceDataGenerator.load_all_invoices()
        match = next((inv for inv in invoices if inv["booking_id"] == booking_id), None)
        if match:
            print("\n--- Invoice ---")
            for key, value in match.items():
                print(f"{key}: {value}")
        else:
            print("Invoice not found for that booking ID.")