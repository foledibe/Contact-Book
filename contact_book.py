import json
import os

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

    def search_contact(self, keyword):
        keyword = keyword.lower()
        results = [c for c in self.contacts if keyword in c.name.lower()]
        if not results:
            print(f"No contacts found matching '{keyword}'.")
        else:
            print(f"\n--- Search results for '{keyword}' ---")
            for contact in results:
                print(contact)
        return results

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Deleted {contact.name}.")
                return
        print(f"No contact named '{name}' found.")

    def edit_contact(self, name, new_phone=None, new_email=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                print(f"Updated {contact.name}.")
                return
        print(f"No contact named '{name}' found.")

    def save_to_file(self, filename="contacts.json"):
        data = [contact.to_dict() for contact in self.contacts]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print("Contacts saved!")

    def load_from_file(self, filename="contacts.json"):
        if not os.path.exists(filename):
            return  # No saved file yet — that's fine, start with an empty book
        with open(filename, "r") as f:
            data = json.load(f)
        self.contacts = [Contact.from_dict(item) for item in data]