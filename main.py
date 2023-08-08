# main.py

import contacts

def print_menu():
    print("Contact Management System")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

def get_user_choice():
    return input("Enter your choice: ")

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    contacts.add_contact(contacts_data, name, phone, email)
    print(f"{name} has been added to contacts.")

def search_contact():
    name = input("Enter the name to search for: ")
    contact = contacts.search_contact(contacts_data, name)
    if contact:
        print(f"Contact found:\nName: {name}\nPhone: {contact['phone']}\nEmail: {contact['email']}")
    else:
        print(f"No contact found with the name {name}.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    contact = contacts.search_contact(contacts_data, name)
    if contact:
        phone = input("Enter the new phone number: ")
        email = input("Enter the new email address: ")
        contacts.update_contact(contacts_data, name, phone, email)
        print(f"{name}'s contact information has been updated.")
    else:
        print(f"No contact found with the name {name}.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    contacts.delete_contact(contacts_data, name)
    print(f"{name} has been deleted from contacts.")

def main():
    global contacts_data
    contacts_data = contacts.load_contacts()

    while True:
        print_menu()
        choice = get_user_choice()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

    contacts.save_contacts(contacts_data)

if __name__ == "__main__":
    main()
