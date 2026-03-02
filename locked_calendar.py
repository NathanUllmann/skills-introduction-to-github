"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE LOCKED CALENDAR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. MONTHS is defined as a constant tuple ().
[ ] 3. Program uses a for loop to display each month.
[ ] 4. 'try' and 'except' blocks catch a TypeError.
[ ] 5. Comments explain why the modification failed.
-----------------------------------------------------------------------
Name: Nathan Ullmann
Date: 02/23/2026
File: locked_calendar.py
-----------------------------------------------------------------------
"""

#  MONTHS is a CONSTANT tuple meaning it shouldnt change
# Tuples are immutable or locked so to say so Python will not allow a edit to any items inside
MONTHS = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)

# display each month using a for loop
print("Months in the locked calendar:")
for month in MONTHS:
    print(month)

print("\nAttempting to modify the locked calendar...")

try:
    # This will fail because tuples cannot be changed once created (like I said)
    MONTHS[0] = "Smarch"
except TypeError:
    # we catch the TypeError so the program does not crash.
    print("ERROR: You cannot modify MONTHS because it is a locked tuple.")