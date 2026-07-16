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
        if not name:
            print("A contact needs a name!")
            return
        if not phone.isdigit():
            print("Phone number should only contain digits.")
            return
        if "@" not in email or "." not in email:
            print("That doesn't look like a valid email address.")
            return

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

def main():
    book = ContactBook()
    book.load_from_file()

    menu = """
===== CONTACT BOOK =====
1. Add a contact
2. View all contacts
3. Search for a contact
4. Edit a contact
5. Delete a contact
6. Save and exit
=========================
"""

    while True:
        print(menu)
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            email = input("Email: ").strip()
            book.add_contact(name, phone, email)

        elif choice == "2":
            book.view_all()

        elif choice == "3":
            keyword = input("Search for: ").strip()
            book.search_contact(keyword)

        elif choice == "4":
            name = input("Name of contact to edit: ").strip()
            new_phone = input("New phone (leave blank to skip): ").strip()
            new_email = input("New email (leave blank to skip): ").strip()
            book.edit_contact(name, new_phone or None, new_email or None)

        elif choice == "5":
            name = input("Name of contact to delete: ").strip()
            book.delete_contact(name)

        elif choice == "6":
            book.save_to_file()
            print("Goodbye!")
            break

        else:
            print("That's not a valid option. Please choose 1-6.")


if __name__ == "__main__":
    main()