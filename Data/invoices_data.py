import json
import os

class InvoiceDataGenerator:
    """Handles generation, saving, and loading of invoice data."""

    FILE_PATH = "invoices_data.json"

    @staticmethod
    def generate_json(booking, invoice_status="issued"):
        """
        Generate invoice data as a dictionary from a booking.

        Args:
            booking (Booking): The booking object.
            invoice_status (str): Invoice status (default is "issued").

        Returns:
            dict: Invoice data.
        """
        nights = (booking.check_out_date - booking.check_in_date).days
        discount = booking.guest.discount(nights)

        invoice = {
            "booking_id": booking.booking_id,
            "guest_name": booking.guest.full_name,
            "guest_id": booking.guest.guest_id,
            "room_type": booking.room.get_typeroom(),
            "room_number": booking.room.number,
            "check_in": str(booking.check_in_date.date()),
            "check_out": str(booking.check_out_date.date()),
            "nights": nights,
            "price_per_night": booking.room.get_price(),
            "discount": f"{discount * 100:.0f}%",
            "total_cost": booking.total_cost,
            "status": booking.status,
            "is_paid": booking.is_paid,
            "invoice_status": invoice_status
        }

        if booking.status == "cancelled":
            invoice["cancellation_fee"] = getattr(booking, "cancellation_fee", 0.0)

        if hasattr(booking.guest, "accumulate_points"):
            points = booking.guest.accumulate_points(nights)
            invoice["points"] = points

        return invoice

    @staticmethod
    def save_json_to_file(booking, invoice_status="issued"):
        """
        Save invoice data to file, updating existing entry if found.

        Args:
            booking (Booking): The booking to generate invoice from.
            invoice_status (str): Status of the invoice.
        """
        new_data = InvoiceDataGenerator.generate_json(booking, invoice_status)

        try:
            with open(InvoiceDataGenerator.FILE_PATH, "r") as f:
                all_data = json.load(f)
        except FileNotFoundError:
            all_data = []

        found = False
        for i, entry in enumerate(all_data):
            if entry["booking_id"] == booking.booking_id:
                all_data[i] = new_data
                found = True
                break

        if not found:
            all_data.append(new_data)

        with open(InvoiceDataGenerator.FILE_PATH, "w") as f:
            json.dump(all_data, f, indent=4)

    @staticmethod
    def load_all_invoices():
        """
        Load all invoice records from file.

        Returns:
            list: List of invoice dictionaries.
        """
        try:
            with open(InvoiceDataGenerator.FILE_PATH, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
