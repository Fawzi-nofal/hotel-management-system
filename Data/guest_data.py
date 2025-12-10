import json
from guest.guest import Regular, VIP, Member

GUEST_TYPE_CLASSES = {
    "regular": Regular,
    "vip": VIP,
    "member": Member
}

class GuestRepository:
    """Handles saving and loading guest data from a JSON file."""

    def __init__(self, filename="guests.json"):
        """Initialize with the filename used to store guests."""
        self.filename = filename

    def load_guests(self):
        """
        Load guest data from the JSON file.

        Returns:
            dict: Dictionary of guest_id -> Guest objects.

        Raises:
            ValueError: If data is invalid or contains unknown guest type.
        """
        try:
            with open(self.filename, "r") as f:
                content = f.read()
                if not content.strip():
                    return {}

                data = json.loads(content)
                guests = {}

                for guest_data in data:
                    if not isinstance(guest_data, dict):
                        continue  # Skip invalid entries

                    guest_type = guest_data.get("type", "").lower()
                    cls = GUEST_TYPE_CLASSES.get(guest_type)
                    if cls is None:
                        raise ValueError(f"Unknown guest type: {guest_type}")

                    guest_id = guest_data.get("guest_id")
                    if not guest_id or not isinstance(guest_id, (int, str)):
                        raise ValueError(f"Invalid or missing guest ID in data: {guest_data}")

                    full_name = guest_data.get("full_name", "")
                    phone = guest_data.get("phone", "")
                    if not full_name or not phone:
                        raise ValueError(f"Missing full_name or phone in data: {guest_data}")

                    guest = cls(guest_id, full_name, phone)

                    if cls == Member:
                        points = guest_data.get("points", 0)
                        if not isinstance(points, (int, float)) or points < 0:
                            raise ValueError(f"Invalid points value for guest {guest_id}: {points}")
                        guest.points = points

                    guests[guest_id] = guest

                return guests

        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in {self.filename}")

    def save_guests(self, guests):
        """
        Save guest data to the JSON file.

        Args:
            guests (dict): Dictionary of Guest objects.
        """
        data = []
        for guest in guests.values():
            guest_data = {
                "guest_id": guest.guest_id,
                "full_name": guest.full_name,
                "phone": guest.phone,
                "type": guest.type_guest()
            }
            if isinstance(guest, Member):
                guest_data["points"] = guest.points
            data.append(guest_data)

        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)
