"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. ATM runs in a "while True" loop to remain awake.
[ ] 3. Main menu uses match-case logic for selections.
[ ] 4. Inputs are validated (e.g., .isdigit()) to prevent crashes.
[ ] 5. Logic prevents overdrafts and negative deposits.
[ ] 6. All currency is formatted to two decimal places (:.2f).
[ ] 7. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
Name: Nathan Ullmann
Date: 02/09/2026
File: atm.py
-----------------------------------------------------------------------
"""

balance = 1000.00

def is_money(text: str) -> bool:
    """
    Returns True if text looks like a valid positive money number (digits or digits.decimals).
    Examples: "10", "10.5", "10.50" are valid. "abc", "-5", "10..2" are not.
    """
    text = text.strip()
    if text.count(".") > 1:
        return False

    # Allow a decimal point
    if "." in text:
        left, right = text.split(".", 1)
        if left == "" or right == "":
            return False
        return left.isdigit() and right.isdigit()

    return text.isdigit()

while True:
    print("\n--- Simple ATM ---")
    print("1) Check Balance")
    print("2) Deposit")
    print("3) Withdraw")
    print("4) Transfer")
    print("5) Exit")

    choice = input("Choose an option (1-5): ").strip()

    match choice:
        case "1":
            print(f"Current balance: ${balance:.2f}")

        case "2":
            amount_text = input("Enter deposit amount: $").strip()

            if not is_money(amount_text):
                print("Invalid amount. Please enter numbers only (example: 25 or 25.50).")
                continue

            amount = float(amount_text)

            if amount <= 0:
                print("Deposit must be greater than $0.00.")
            else:
                balance += amount
                print(f"Deposit successful. New balance: ${balance:.2f}")

        case "3":
            amount_text = input("Enter withdrawal amount: $").strip()

            if not is_money(amount_text):
                print("Invalid amount. Please enter numbers only (example: 25 or 25.50).")
                continue

            amount = float(amount_text)

            if amount <= 0:
                print("Withdrawal must be greater than $0.00.")
            elif amount > balance:
                print("Insufficient funds. Overdrafts are not allowed.")
                print(f"Current balance: ${balance:.2f}")
            else:
                balance -= amount
                print(f"Withdrawal successful. New balance: ${balance:.2f}")

        case "4":
            amount_text = input("Enter transfer amount: $").strip()

            if not is_money(amount_text):
                print("Invalid amount. Please enter numbers only (example: 25 or 25.50).")
                continue

            amount = float(amount_text)

            if amount <= 0:
                print("Transfer must be greater than $0.00.")
            elif amount > balance:
                print("Insufficient funds. Transfer denied.")
                print(f"Current balance: ${balance:.2f}")
            else:
                balance -= amount
                print(f"Transfer successful. New balance: ${balance:.2f}")

        case "5":
            print("Goodbye!")
            break

        case _:
            print("Invalid selection. Please choose 1-5.")