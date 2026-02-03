"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator
DATE: 02/02/2026
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask user for their age (convert to int).
2. Use if/elif/else to determine price:
   - Under 1: FREE ($0.00)
   - 1 to 11: $1.00 per year of age (Example: 5 years = $5.00)
   - 12 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. Print the final price formatted as currency (e.g., $16.95).
-----------------------------------------------------------------------
"""

# Ask for age and then convert it to a int
age = int(input("Please Enter your age: "))

# Figure out price based on the age
if age < 1:
   if age < 1:
    price = 0.00
elif age <= 11:
    price = float(age)  # $1 per year
elif age <= 64:
    price = 16.95
else:
    price = 12.95

# Then print as currency
print(f"Your buffet price is ${price:.2f}")