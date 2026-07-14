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
    
class ContactBook:
    """Manages a collection of Contact objects."""

    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        print(f"Added {name} to your contact book!")

    def view_all(self):
        if not self.contacts:
            print("Your contact book is empty.")
            return
        print("\n--- All Contacts ---")
        for index, contact in enumerate(self.contacts, start=1):
            print(f"{index}. {contact}") 
