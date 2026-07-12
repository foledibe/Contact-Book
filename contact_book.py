class Contact:
    """Represents a single contact with a name, phone number, and email."""

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        """This controls how a Contact looks when we print it."""
        return f"{self.name} | Phone: {self.phone} | Email: {self.email}"

    def to_dict(self):
        """Convert this contact into a plain dictionary, so we can save it as JSON."""
        return {"name": self.name, "phone": self.phone, "email": self.email}

    @classmethod
    def from_dict(cls, data):
        """Build a Contact object back from a dictionary (used when loading from file)."""
        return cls(data["name"], data["phone"], data["email"])