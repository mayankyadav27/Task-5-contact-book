contact_book = {}

# Function to add a new contact
def add_contact(name, phone, email):
    contact_book[name] = {'phone': phone, 'email': email}
    print(f"Contact {name} added successfully.")

# Function to view all contacts
def view_contacts():
    if contact_book:
        for name, info in contact_book.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("No contacts found.")

# Function to search for a contact
def search_contact(name):
    if name in contact_book:
        print(f"Name: {name}, Phone: {contact_book[name]['phone']}, Email: {contact_book[name]['email']}")
    else:
        print(f"No contact found with the name {name}.")

# Function to update a contact
def update_contact(name, phone=None, email=None):
    if name in contact_book:
        if phone:
            contact_book[name]['phone'] = phone
        if email:
            contact_book[name]['email'] = email
        print(f"Contact {name} updated successfully.")
    else:
        print(f"No contact found with the name {name}.")

# Function to delete a contact
def delete_contact(name):
    if name in contact_book:
        del contact_book[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"No contact found with the name {name}.")

# Main program loop
def main():
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_contact(name, phone, email)
        
        elif choice == '2':
            view_contacts()
        
        elif choice == '3':
            name = input("Enter the name to search: ")
            search_contact(name)
        
        elif choice == '4':
            name = input("Enter the name to update: ")
            phone = input("Enter new phone number (leave blank if no change): ")
            email = input("Enter new email (leave blank if no change): ")
            update_contact(name, phone if phone else None, email if email else None)
        
        elif choice == '5':
            name = input("Enter the name to delete: ")
            delete_contact(name)
        
        elif choice == '6':
            print("Exiting contact book.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
