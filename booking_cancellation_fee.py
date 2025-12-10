from datetime import datetime
from calculate_total_cost import BookingCostCalculator

class BookingCancellationCalculator:
    @staticmethod
    def calculate_cancellation_fee(booking):
        """Calculate cancellation fee based on days before check-in."""
        if booking.status.lower() != "cancelled":
            return 0.0

        today = datetime.today().date()
        days_before_checkin = (booking.check_in_date.date() - today).days
        total_cost = BookingCostCalculator.calculate_total_cost(booking)

        if days_before_checkin > 7:
            return 0.0
        elif 0 < days_before_checkin <= 7:
            return total_cost * 0.3
        else:
            return total_cost
