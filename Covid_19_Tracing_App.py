# Anonuevo, Loraine N.
# BSCPE 1-4

import csv

# Function to add an entry to the contact tracing app
def add_entry():
    name = input("Enter full name: ")
    phone = input("Enter phone number: ")
    date = input("Enter date of contact (YYYY-MM-DD): ")
    location = input("Enter location of contact: ")
    
    with open("contact_tracing.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, date, location])
    
    print("Entry added successfully!")

# Function to search for entries in the contact tracing app
def search_entry():
    search_term = input("Enter the name or phone number to search: ")
    
    with open("contact_tracing.csv", "r") as file:
        reader = csv.reader(file)
        found_entries = []
        for row in reader:
            if search_term.lower() in [item.lower() for item in row]:
                found_entries.append(row)
    
    if found_entries:
        print("Found entries:")
        for entry in found_entries:
            print("Name:", entry[0])
            print("Phone:", entry[1])
            print("Date of contact:", entry[2])
            print("Location of contact:", entry[3])
            print("--------------------")
    else:
        print("No entries found.")
