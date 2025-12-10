from abc import ABC, abstractmethod

class PriceStrategy(ABC):
    """Abstract base class for room pricing strategies."""
    @abstractmethod
    def calculate_price(self, base_price):
        """
        Calculates the final price based on a given base price.
        Must be implemented by subclasses.
        """
        pass

class RegularSeasonStrategy(PriceStrategy):
    """Applies no change to the base price (regular season)."""

    def calculate_price(self, base_price):
        """Returns the base price unchanged."""
        return base_price

class PeakSeasonStrategy(PriceStrategy):
    """Increases the base price by 50% (peak season)."""

    def calculate_price(self, base_price):
        """Returns the base price with a 50% increase."""
        return base_price * 1.5

class WinterDiscountStrategy(PriceStrategy):
    """Reduces the base price by 20% (winter discount)."""

    def calculate_price(self, base_price):
        """Returns the base price with a 20% discount."""
        return base_price * 0.8
