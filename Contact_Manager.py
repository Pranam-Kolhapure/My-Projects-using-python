import os

contacts = {}

# Load contacts from file
def load_contacts():
    if os.path.exists("contacts.txt"):
        file = open("contacts.txt", "r")
        for line in file:
            line = line.strip()
            if line:
                name, number = line.split(",")
                contacts[name] = number
        file.close()

# Save contacts to file
def save_contacts():
    file = open("contacts.txt", "w")
    for name, number in contacts.items():
        file.write(name + "," + number + "\n")
    file.close()

# Add Contact
def add_contact():
    name = input("Enter Name: ")
    number = input("Enter Contact Number: ")
    contacts[name] = number
    save_contacts()
    print("Contact Added Successfully!")

# View Contacts
def view_contacts():
    if len(contacts) == 0:
        print("No Contacts Found!")
    else:
        print("\nContacts List")
        print("------------------------")
        for name, number in contacts.items():
            print("Name:", name)
            print("Number:", number)
            print("------------------------")

# Update Contact
def update_contact():
    name = input("Enter Name to Update: ")
    if name in contacts:
        number = input("Enter New Contact Number: ")
        contacts[name] = number
        save_contacts()
        print("Contact Updated Successfully!")
    else:
        print("Contact Not Found!")

# Delete Contact
def delete_contact():
    name = input("Enter Name to Delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts()
        print("Contact Deleted Successfully!")
    else:
        print("Contact Not Found!")

# Main Program
load_contacts()

while True:
    print("\n===== Contact Management System =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")