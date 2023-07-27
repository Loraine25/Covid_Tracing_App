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
