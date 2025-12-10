from abc import ABC, abstractmethod
from guest.guest import Regular, VIP, Member 

class GuestFactory:
    """Factory for creating guest objects by type."""

    MAP = {
        "regular": Regular,
        "vip": VIP,
        "member": Member
    }

    @staticmethod
    def create(guest_type, guest_id, full_name, phone):
        """
        Create a guest object based on type.

        Args:
            guest_type (str): Type of guest ("regular", "vip", "member").
            guest_id (str): Guest ID.
            full_name (str): Guest's full name.
            phone (str): Guest's phone number.

        Returns:
            Guest: An instance of the appropriate guest subclass.

        Raises:
            ValueError: If the guest type is unknown.
        """
        guest_type = guest_type.lower()
        if guest_type not in GuestFactory.MAP:
            raise ValueError(f"Guest type '{guest_type}' not found")
        cls = GuestFactory.MAP[guest_type]
        if guest_type == "member":
            return cls(guest_id, full_name, phone, points=0)
        return cls(guest_id, full_name, phone)
