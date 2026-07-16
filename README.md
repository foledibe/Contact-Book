# Contact Book

A command-line contact book built in Python. Add, view, search, edit, and delete
contacts, with data saved automatically to a local file so nothing is lost
between runs.

## Features

- Add new contacts (name, phone, email)
- View all contacts
- Search contacts by name
- Edit existing contacts
- Delete contacts
- Contacts are saved to `contacts.json` automatically

## How to run

```bash
python contact_book.py
```

You'll see a menu where you can add, view, search, edit, or delete contacts.
All contacts are automatically saved to `contacts.json` in the same folder,
so your data is still there next time you run the program.

## Example

```
===== CONTACT BOOK =====
1. Add a contact
2. View all contacts
3. Search for a contact
4. Edit a contact
5. Delete a contact
6. Save and exit
=========================
Choose an option (1-6): 1
Name: Sam Rivera
Phone: 5551234567
Email: sam@example.com
Added Sam Rivera to your contact book!
```

## What I learned building this

- Structuring a program with classes (`Contact`, `ContactBook`)
- Reading/writing JSON files for data persistence
- Building an interactive command-line menu
- Basic input validation

## Author

Built by Fiorella Oledibe as a portfolio project.
