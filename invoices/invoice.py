from Data.invoices_data import InvoiceDataGenerator

class Invoice:
    """Class for representing and retrieving invoice data."""

    def __init__(self, data):
        """Initialize invoice with given data dictionary."""
        self.data = data

    def __str__(self):
        """Return a formatted string of the invoice details."""
        result = (
            f"Invoice for Booking ID: {self.data['booking_id']}\n"
            f"Guest: {self.data['guest_name']} (ID: {self.data['guest_id']})\n"
            f"Room: {self.data['room_number']} ({self.data['room_type']})\n"
            f"Dates: {self.data['check_in']} to {self.data['check_out']} ({self.data['nights']} nights)\n"
            f"Price per Night: {self.data['price_per_night']}₪\n"
            f"Discount: {self.data['discount']*100:.0f}%\n"
            f"Total Cost: {self.data['total_cost']}₪\n"
            f"Cancellation Fee: {self.data.get('cancellation_fee', 0.0)}₪\n"
            f"Paid: {'Yes' if self.data['is_paid'] else 'No'}\n"
            f"Invoice Status: {self.data['invoice_status']}"
        )
        if "points" in self.data:
            result += f"\nPoints: {self.data['points']}"
        return result

    @staticmethod
    def find_by_booking_id(booking_id):
        """
        Find and return an invoice by booking ID.

        Args:
            booking_id (str): The booking ID to search for.

        Returns:
            Invoice or None: Invoice object if found, else None.
        """
        all_invoices = InvoiceDataGenerator.load_all_invoices()
        for data in all_invoices:
            if data["booking_id"] == booking_id:
                return Invoice(data)
        return None

    @staticmethod
    def find_by_status(status):
        """
        Find all invoices by status (e.g., issued, paid, cancelled).

        Args:
            status (str): Invoice status to search by.

        Returns:
            list: List of Invoice objects with matching status.
        """
        all_invoices = InvoiceDataGenerator.load_all_invoices()
        status = status.lower()
        return [Invoice(data) for data in all_invoices if data.get("invoice_status", "").lower() == status]
