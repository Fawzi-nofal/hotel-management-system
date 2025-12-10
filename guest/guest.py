from abc import ABC, abstractmethod

class Guest(ABC):
    """Abstract base class for a hotel guest."""

    def __init__(self, guest_id, full_name, phone):
        """Initialize a guest with ID, full name, and phone number."""
        self.guest_id = guest_id
        self.full_name = full_name
        self.phone = phone

    @abstractmethod
    def type_guest(self):
        """Returns the type of the guest."""
        pass

    @abstractmethod
    def discount(self, nights=0):
        """Returns the discount percentage based on guest type."""
        pass

    def update_details(self, name=None, phone=None):
        """Update the guest's name and/or phone number."""
        if name is not None:
            self.full_name = name
        if phone is not None:
            self.phone = phone

    def __str__(self):
        """Return a string with guest details."""
        return (
            f"ID: {self.guest_id}\n"
            f"Full name: {self.full_name}\n"
            f"Phone number: {self.phone}\n"
            f"Guest type: {self.type_guest()}"
        )

class Regular(Guest):
    """Regular guest with no discount."""

    def type_guest(self):
        """Returns 'Regular' as guest type."""
        return "Regular"

    def discount(self, nights=0):
        """Returns 0% discount."""
        return 0.0

class VIP(Guest):
    """VIP guest with fixed discount."""

    def type_guest(self):
        """Returns 'VIP' as guest type."""
        return "VIP"

    def discount(self, nights=0):
        """Returns 30% discount."""
        return 0.3

class Member(Guest):
    """Member guest with point accumulation and conditional discount."""

    def __init__(self, guest_id, full_name, phone, points=0):
        """Initialize a member guest with optional starting points."""
        super().__init__(guest_id, full_name, phone)
        self.points = points

    def accumulate_points(self, nights):
        """
        Add points based on number of nights.
        Extra bonus points if staying more than 5 nights.
        """
        if not isinstance(nights, int) or nights < 0:
            raise ValueError("Nights must be a non-negative integer")
        self.points += nights
        if nights > 5:
            self.points += 10
        return self.points

    def discount(self, nights=0):
        """Returns 10% discount if points are at least 100."""
        if self.points >= 100:
            return 0.1
        return 0.0

    def type_guest(self):
        """Returns 'Member' as guest type."""
        return "Member"

    def __str__(self):
        """Return guest details with points."""
        base = super().__str__()
        return base + f"\nPoints: {self.points}"
