# create a dictionary with initial data
phone_book = {"John": "1234567", "Smith": "9876543"}

# function to add a contact
def add_contact(name, phone, phone_book):
    phone_book[name] = phone
    print("Contact added successfully.")

# function to modify a contact
def modify_contact(name, new_phone, phone_book):
    if name in phone_book:
        phone_book[name] = new_phone
        print("Contact modified successfully.")
    else:
        print("Contact not found.")

# function to delete a contact
def delete_contact(name, phone_book):
    if name in phone_book:
        del phone_book[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

# function to print the list of contacts
def print_contact_list(phone_book):
    for name, phone in phone_book.items():
        print(f"{name}: {phone}")
