"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
Name: Nathan Ullmann
Date: 02/23/2026
File: tickets.py
-----------------------------------------------------------------------
"""

seats = list(range(1, 21))   # seats 1 through 20

while True:
    # If no seats left then end the program
    if len(seats) == 0:
        print("All seats are sold out!")
        break

    print(f"\nAvailable seats: {seats}")
    choice = int(input("Pick a seat number (1-20) or 0 to quit: "))

    # exit switch
    if choice == 0:
        print("Goodbye!")
        break

    # Membership check
    if choice in seats:
        seats.remove(choice)
        print(f"Seat {choice} purchased!")
    else:
        print("That seat is taken or doesn't exist. Try another one.")