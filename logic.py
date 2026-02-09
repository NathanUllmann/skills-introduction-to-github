"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
Name: Nathan Ullmann
Date: 02/09/2026
File: logic.py
-----------------------------------------------------------------------
"""

num1 = int(input("Enter num1 (integer): "))
num2 = int(input("Enter num2 (integer): "))

# my 6 logical checks
both_over_0 = (num1 > 0) and (num2 > 0)
both_over_100 = (num1 > 100) and (num2 > 100)
either_even = (num1 % 2 == 0) or (num2 % 2 == 0)
either_less_100 = (num1 < 100) or (num2 < 100)
not_equal = (num1 != num2)
not_zero = (num1 != 0) and (num2 != 0)

print("\n--- Boolean Checks ---")
print(f"Both > 0: {both_over_0}")
print(f"Both > 100: {both_over_100}")
print(f"Either Even: {either_even}")
print(f"Either < 100: {either_less_100}")
print(f"Not Equal: {not_equal}")
print(f"Not Zero: {not_zero}")

# categorize the num1
print("\n--- num1 Category ---")
if num1 > 0:
    print("num1 is Positive")
elif num1 < 0:
    print("num1 is Negative")
else:
    print("num1 is Zero")