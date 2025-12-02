# %%
"""
=====================================================
 DATA STRUCTURES AND ALGORITHMS — MIDTERM EXAM
=====================================================
Mini-Project: CONTACT LIST MANAGEMENT SYSTEM
Student Name: Tyrone Tabornal
Section: BSIT 2-A
Date: October 28, 2025

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
    """A class to represent a single contact."""

    def __init__(self, name, mobile, email):
        """Initializes a Contact object with name, mobile number, and email."""
        self.name = name
        self.mobile = mobile
        self.email = email
    
    def get_name(self):
        """Returns the contact's name."""
        return self.name
    
    def get_mobile(self):
        """Returns the contact's mobile number."""
        return self.mobile
    
    def get_email(self):
        """Returns the contact's email address."""
        return self.email
    
    def __str__(self):
        """Returns a user-friendly string representation of the contact."""
        return f"  Name  : {self.name}\n  Mobile: {self.mobile}\n  Email : {self.email}"


class ContactList:
    """A class to manage a list of contacts using a Python list (array)."""

    def __init__(self):
        """Initializes an empty contact list."""
        self.contacts = []

    def __is_empty(self):
        """A private helper method to check if the contact list is empty."""
        return len(self.contacts) == 0

    def __find_contact_index(self, name):
        """
        A private helper method to find a contact's index by name (case-insensitive).
        This avoids code duplication in the search_contact and delete_contact methods.
        """
        for i, contact in enumerate(self.contacts):
            if contact.get_name().lower() == name.lower():
                return i  # Return the index if found
        return None  # Return None if not found

    def add_contact(self, name, mobile, email):
        """Creates a new Contact object and adds it to the list."""
        new_contact = Contact(name, mobile, email)
        self.contacts.append(new_contact)
        print(f"\nSuccess: '{name}' has been added to your contacts.")

    def display_contacts(self):
        """Displays all contacts currently in the list."""
        print("\n--- All Contacts ---")
        if self.__is_empty():
            print("Your contact list is empty. Add a contact to get started!")
        else:
            print(f"Showing {len(self.contacts)} contact(s):\n")
            for i, contact in enumerate(self.contacts, 1):
                print(f"Contact #{i}:\n{contact}")
                # Print a separator for better readability between contacts
                if i < len(self.contacts):
                    print("-" * 20)
        print("--------------------")

    def search_contact(self, name):
        """Searches for a contact by name and displays their information if found."""
        print(f"\nSearching for '{name}'...")
        index = self.__find_contact_index(name)
        if index is not None:
            print("Contact found!")
            print(self.contacts[index])
        else:
            print(f"No contact found with the name '{name}'.")

    def delete_contact(self, name):
        """Deletes a contact from the list by name."""
        print(f"\nAttempting to delete '{name}'...")
        index = self.__find_contact_index(name)
        if index is not None:
            self.contacts.pop(index)
            print(f"Success: '{name}' has been deleted from your contacts.")
        else:
            print(f"Cannot delete. No contact found with the name '{name}'.")


# Main Program Execution
if __name__ == "__main__":
    contact_list = ContactList()
    
    while True:
        print("""
==================================
   CONTACT LIST MANAGEMENT SYSTEM
==================================
[1] Add Contact
[2] Display All Contacts
[3] Search Contact
[4] Delete Contact
[5] Exit
==================================""")

        try:
            choice = int(input("Enter your choice [1-5]: "))

            if choice == 1:
                print("\n--- Add New Contact ---")
                # Loop to ensure the user provides a non-empty name
                name = ""
                while not name.strip():
                    name = input("Enter Name: ")
                    if not name.strip():
                        print("Name cannot be empty. Please try again.")
                
                # Mobile number is stored as a string to support various formats and leading zeros
                mobile = input(f"Enter {name}'s Mobile Number: ")
                email = input(f"Enter {name}'s Email Address: ")
                
                # Call the method to add the contact
                contact_list.add_contact(name, mobile, email)

            elif choice == 2:
                contact_list.display_contacts()

            elif choice == 3:
                print("\n--- Search for a Contact ---")
                name = input("Enter the name of the contact to search for: ")
                contact_list.search_contact(name)

            elif choice == 4:
                print("\n--- Delete a Contact ---")
                name = input("Enter the name of the contact to delete: ")
                contact_list.delete_contact(name)
            
            elif choice == 5:
                # The 'break' statement correctly terminates the while loop, ending the program.
                print("\nThank you for using the system. Goodbye!")
                break

            else:
                # Handles cases where the user enters a number outside the 1-5 range
                print("\nInvalid choice. Please enter a number between 1 and 5.")
        
        except ValueError:
            # Catches errors if the user enters text instead of a number
            print("\nInvalid input. Please enter a number.")
# %%