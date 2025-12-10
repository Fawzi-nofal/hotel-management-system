class BookingCostCalculator:
    @staticmethod
    def calculate_total_cost(booking):
        """Calculate total cost with guest discount applied."""
        nights = (booking.check_out_date - booking.check_in_date).days
        base_cost = nights * booking.room.get_price()
        discount = booking.guest.discount(nights)
        return base_cost * (1 - discount)
