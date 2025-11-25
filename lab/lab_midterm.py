"""
=====================================================
 DATA STRUCTURES AND ALGORITHMS — MIDTERM EXAM
=====================================================
Mini-Project: CONTACT LIST MANAGEMENT SYSTEM
Student Name: _______________________
Section: ____________________________
Date: _______________________________

Instructions:
1. Follow the project description and requirements below.
2. Write all your code in this file.
3. Do not import external libraries. Use only built-in Python features.
4. You may refer to your notes, but no internet search or communication.
5. Save and submit this file before the time ends.

=====================================================
PROJECT DESCRIPTION
=====================================================
Create a Contact List Management System using an Array (Python list).

Each contact should have:
- Name
- Mobile Number
- Email Address

Your program should implement two classes:
1. Contact
   - name
   - mobile
   - email
2. ContactList
   - add_contact(name, mobile, email)
   - display_contacts()
   - search_contact(name)
   - delete_contact(name)

Menu Options:
[1] Add Contact
[2] Display All Contacts
[3] Search Contact
[4] Delete Contact
[5] Exit

=====================================================
Evaluation (100%)
- Functionality: 40%
- Code Organization: 25%
- Array Implementation: 25%
- User Interface & Documentation: 10%
=====================================================
"""

# =====================================================
# START CODING BELOW
# =====================================================

class Contact:
    def __init__(self, name, mobile, email):
        pass  # TODO: Initialize attributes


class ContactList:
    def __init__(self):
        pass  # TODO: Initialize an empty list for contacts

    def add_contact(self, name, mobile, email):
        pass  # TODO: Add a new contact to the list

    def display_contacts(self):
        pass  # TODO: Display all contacts

    def search_contact(self, name):
        pass  # TODO: Search contact by name

    def delete_contact(self, name):
        pass  # TODO: Delete contact by name


# Main Program
if __name__ == "__main__":
    contact_list = ContactList()
    while True:
        print("""
==================================
     CONTACT LIST MANAGEMENT
==================================
[1] Add Contact
[2] Display All Contacts
[3] Search Contact
[4] Delete Contact
[5] Exit
==================================
""")
        choice = input("Enter choice: ")

        # TODO: Implement menu actions here