"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 4 inputs have 'while' loop validation.
[ ] 3. The Chaperone loop uses .upper() and correct Boolean logic.
[ ] 4. I have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
Name: Nathan Ullmann
Date: 02/09/2026
File: registration.py
-----------------------------------------------------------------------
"""

# First Name (cannot be blank)
first_name = input("Enter First Name: ").strip()
while first_name == "":
    print("Error: First name cannot be blank.")
    first_name = input("Enter First Name: ").strip()

# Last Name (cannot be blank)
last_name = input("Enter Last Name: ").strip()
while last_name == "":
    print("Error: Last name cannot be blank.")
    last_name = input("Enter Last Name: ").strip()

# Chaperone (Y/N only, uses .upper() and correct boolean logic)
chaperone = input("Parent volunteering to chaperone? (Y/N): ").strip().upper()
while chaperone != "Y" and chaperone != "N":
    print("Error: Please enter Y or N.")
    chaperone = input("Parent volunteering to chaperone? (Y/N): ").strip().upper()

# Phone Number (cant be nothing)
phone_number = input("Enter Phone Number: ").strip()
while phone_number == "":
    print("Error: Phone number cannot be blank.")
    phone_number = input("Enter Phone Number: ").strip()

# Ticket Count (must be integer > 0, made it crash proof with try/except)
ticket_count = 0
while True:
    try:
        ticket_count = int(input("How many tickets? "))
        if ticket_count > 0:
            break
        print("Error: Ticket count must be at least 1.")
    except ValueError:
        print("Error: Please enter a NUMBER (ex: 3).")

print("\nRegistration Complete!")
print(f"Name: {first_name} {last_name}")
print(f"Chaperone: {chaperone}")
print(f"Phone: {phone_number}")
print(f"Tickets: {ticket_count}")