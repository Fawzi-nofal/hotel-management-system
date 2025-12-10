import unittest
from invoices.invoice import Invoice

class TestInvoice(unittest.TestCase):
    def setUp(self):
        self.sample_data = {
            "booking_id": "123",
            "guest_name": "John Doe",
            "guest_id": "456",
            "room_type": "Standard",
            "room_number": 101,
            "check_in": "2025-06-01",
            "check_out": "2025-06-05",
            "nights": 4,
            "price_per_night": 200,
            "discount": 0.1,
            "total_cost": 720.0,
            "status": "confirmed",
            "is_paid": True,
            "cancellation_fee": 0.0,
            "invoice_status": "issued"
        }
        self.invoice = Invoice(self.sample_data)

    def test_invoice_str_contains_guest_name(self):
        self.assertIn("John Doe", str(self.invoice))

    def test_invoice_discount_display(self):
        output = str(self.invoice)
        self.assertIn("10%", output)

    def test_get_invoice_id(self):
        self.assertEqual(self.invoice.data["booking_id"], "123")

if __name__ == "__main__":
    unittest.main()
