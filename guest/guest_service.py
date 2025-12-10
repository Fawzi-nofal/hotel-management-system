from Data.guest_data import GuestRepository
from guest.guest_factory import GuestFactory

class GuestService:
    """Service class for managing guests in the system."""

    def __init__(self, repository=None):
        """Initialize with repository and load guests."""
        self.repository = repository or GuestRepository()
        self.guests = self.repository.load_guests()

    def add_guest(self, type_guest, guest_id, full_name, phone):
        """Add a new guest to the system."""
        self.guest_not_exists(guest_id)
        new_guest = GuestFactory.create(type_guest, guest_id, full_name, phone)
        self.guests[guest_id] = new_guest
        self.repository.save_guests(self.guests)
        return f"Guest {guest_id} added as {type_guest}."

    def remove_guest(self, guest_id):
        """Remove a guest by ID."""
        self.guest_exists(guest_id)
        del self.guests[guest_id]
        self.repository.save_guests(self.guests)
        return f"Guest with ID {guest_id} was successfully removed."

    def update_guest_info(self, guest_id, new_full_name=None, new_phone=None):
        """Update guest name or phone."""
        self.guest_exists(guest_id)
        guest = self.guests[guest_id]
        guest.update_details(name=new_full_name, phone=new_phone)
        self.repository.save_guests(self.guests)
        return f"Guest {guest_id} updated successfully."

    def update_guest_type(self, guest_id, new_type):
        """Change the guest type (e.g., from regular to VIP)."""
        self.guest_exists(guest_id)
        old_guest = self.guests[guest_id]
        new_guest = GuestFactory.create(new_type, old_guest.guest_id, old_guest.full_name, old_guest.phone)

        if hasattr(old_guest, "points") and hasattr(new_guest, "points"):
            new_guest.points = old_guest.points

        self.guests[guest_id] = new_guest
        self.repository.save_guests(self.guests)
        return f"Guest {guest_id} type updated to {new_type}."

    def find_guest_by_id(self, guest_id):
        """Find and return guest by ID."""
        self.guest_exists(guest_id)
        return self.guests[guest_id]

    def guest_exists(self, guest_id):
        """Raise error if guest does not exist."""
        if guest_id not in self.guests:
            raise Exception(f"Guest with ID {guest_id} not found.")

    def guest_not_exists(self, guest_id):
        """Raise error if guest already exists."""
        if guest_id in self.guests:
            raise Exception(f"Guest with ID {guest_id} already exists.")

    def list_all_guests(self):
        """Return list of all guests."""
        return list(self.guests.values())
