"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
Assignment: 4B Loops
Date: 02/09/2026
File: loops.py
-----------------------------------------------------------------------
"""

# ----------------------------
# Task 1: While Loop (The Nagging Kid)
# ----------------------------
keep_asking = True  # boolean control variable

while keep_asking:
    answer = input("Are we there yet? ")

    if answer.lower() == "yes":
        keep_asking = False

print("Yay! We made it.\n")

# ----------------------------
# Task 2: For Loop (99 Bottles of beer on the wall)
# ----------------------------
for number in range(99, 0, -1):
    print(f"{number} bottles of beer on the wall!")