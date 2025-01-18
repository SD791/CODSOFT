contacts = {}

def add_contact(name, phone_number, email, address):
    contacts[name] = {
        'phone_number': phone_number,
        'email': email,
        'address': address
    }
    print(f"Contact {name} added successfully.")

def view_contacts():
    if len(contacts) == 0:
        print("No contacts available.")
    else:
        for name, details in contacts.items():
            print(f"Name: {name}, Phone_number: {details['phone_number']},")

def search_contact(query):
    results = {name: details for name, details in contacts.items() if query.lower() in name.lower() or query in details['phone_number']}
    if results:
        for name, details in results.items():
            print(f"Name: {name}, Phone_number: {details['phone_number']}, Email: {details['email']}, Address: {details['address']}")
    else:
        print("No contacts found.")

def update_contact(name, phone_number=None, email=None, address=None):
    if name in contacts:
            phone_number = input(f"Enter new phone number for {name} (leave blank to keep the current one): ")
            email = input(f"Enter new email for {name} (leave blank to keep the current one): ")
            address = input(f"Enter new address for {name} (leave blank to keep the current one): ")
    if phone_number:
        contacts[name]['phone_number'] = phone_number
    if email:
        contacts[name]['email'] = email
    if address:
        contacts[name]['address'] = address
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact {name} not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")

def main():
    while True:
        print("\nContact Book Application")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone_number, email, address)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            search_contact(query)
        elif choice == '4':
            
            update_contact(name, phone_number if phone_number else None, email if email else None, address if address else None)
        elif choice == '5':
            name = input("Enter name of the contact to delete: ")
            delete_contact(name)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

