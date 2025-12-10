
import unittest
from booking.booking import Booking
from guest.guest import Regular
from room.room import Standard
from datetime import datetime, timedelta
from Data.invoices_data import InvoiceDataGenerator
import os
import json

class TestInvoiceGeneration(unittest.TestCase):
    def setUp(self):
        self.file_path = InvoiceDataGenerator.FILE_PATH
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_invoice_saved_correctly(self):
        guest = Regular("G123", "Test Guest", "0500000000")
        room = Standard(101)
        check_in = datetime.today() + timedelta(days=1)
        check_out = check_in + timedelta(days=4)

        booking = Booking("B002", guest, room, check_in.strftime("%Y-%m-%d"), check_out.strftime("%Y-%m-%d"))
        booking.mark_as_paid()

        InvoiceDataGenerator.save_json_to_file(booking, invoice_status="paid")

        with open("invoices_data.json", "r") as f:
            data = json.load(f)

        invoice = next((inv for inv in data if inv["booking_id"] == "B002"), None)
        self.assertIsNotNone(invoice)
        self.assertEqual(invoice["is_paid"], True)
        self.assertEqual(invoice["invoice_status"], "paid")


    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
