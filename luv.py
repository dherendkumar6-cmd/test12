import sys

def atm_system():
    # Initial account settings
    correct_pin = "1234"
    balance = 1000.00
    max_attempts = 3

    print("====================================")
    print("       WELCOME TO PYTHON BANK       ")
    print("====================================")

    # FOR LOOP 1: Limit PIN authentication to 3 attempts
    pin_authenticated = False
    for attempt in range(1, max_attempts + 1):
        entered_pin = input(f"Enter your 4-digit PIN (Attempt {attempt}/{max_attempts}): ")
        
        if entered_pin == correct_pin:
            print("\nPIN Verified Successfully!\n")
            pin_authenticated = True
            break
        else:
            remaining = max_attempts - attempt
            if remaining > 0:
                print(f"Incorrect PIN. You have {remaining} attempt(s) left.\n")
            else:
                print("\nToo many incorrect attempts. Your card is locked!")
                return

    # If PIN was correct, proceed to transaction menu
    if pin_authenticated:
        max_transactions = 5
        
        # FOR LOOP 2: Limit user to a fixed number of menu transactions
        for t_count in range(1, max_transactions + 1):
            print("------------------------------------")
            print(f"Transaction {t_count} of {max_transactions}")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            print("------------------------------------")
            
            choice = input("Select an option (1-4): ")

            if choice == "1":
                print(f"\nYour current balance is: ${balance:.2f}")

            elif choice == "2":
                amount = float(input("\nEnter deposit amount: $"))
                if amount > 0:
                    balance += amount
                    print(f"Successfully deposited ${amount:.2f}")
                    print(f"Updated Balance: ${balance:.2f}")
                else:
                    print("Invalid amount!")

            elif choice == "3":
                amount = float(input("\nEnter withdrawal amount: $"))
                if amount > balance:
                    print("Insufficient funds!")
                elif amount <= 0:
                    print("Invalid amount!")
                else:
                    balance -= amount
                    print(f"Successfully withdrew ${amount:.2f}")
                    print(f"Remaining Balance: ${balance:.2f}")

            elif choice == "4":
                print("\nThank you for banking with us. Goodbye!")
                break
            else:
                print("Invalid choice! Please select 1, 2, 3, or 4.")

            # Ask if they want another transaction
            if t_count < max_transactions:
                cont = input("\nWould you like another transaction? (y/n): ").strip().lower()
                if cont != 'y':
                    print("\nThank you for using our ATM. Goodbye!")
                    break
        else:
            print("\nYou have reached your maximum transaction limit for this session.")

if __name__ == "__main__":
    atm_system()