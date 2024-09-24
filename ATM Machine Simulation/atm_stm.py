class ATMSimulation:
    def __init__(self):
        # Initialize the ATM with a default balance, default PIN, and an empty transaction history
        self.balance = 1000.0
        self.pin = "1818"
        self.transaction_history = []

    def check_pin(self):
        # Ask the user to enter the PIN and validate it
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN. Please try again.")
            return False

    def balance_inquiry(self):
        # Display the current balance
        print(f"Your current balance is: ${self.balance:.2f}")
        self.transaction_history.append(f"Balance Inquiry: ${self.balance:.2f}")

    def withdraw_cash(self):
        # Ask the user for the withdrawal amount and process the withdrawal
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Withdrawal amount must be greater than zero.")
            elif amount > self.balance:
                print("Insufficient balance.")
            else:
                self.balance -= amount
                print(f"Withdrawal successful. Your new balance is: ${self.balance:.2f}")
                self.transaction_history.append(f"Withdrawal: -${amount:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def deposit_cash(self):
        # Ask the user for the deposit amount and process the deposit
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Deposit amount must be greater than zero.")
            else:
                self.balance += amount
                print(f"Deposit successful. Your new balance is: ${self.balance:.2f}")
                self.transaction_history.append(f"Deposit: +${amount:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def change_pin(self):
        # Ask the user to enter the new PIN and confirm it
        new_pin = input("Enter new PIN: ")
        confirm_pin = input("Confirm new PIN: ")
        if new_pin == confirm_pin:
            self.pin = new_pin
            print("PIN change successful.")
            self.transaction_history.append("PIN Change: Successful")
        else:
            print("PINs do not match. Please try again.")

    def view_transaction_history(self):
        # Display the transaction history
        if not self.transaction_history:
            print("No transactions found.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)

    def main_menu(self):
        # Display the main menu and handle user choices
        while True:
            print("\n----- ATM Main Menu -----")
            print("1. Balance Inquiry")
            print("2. Withdraw Cash")
            print("3. Deposit Cash")
            print("4. Change PIN")
            print("5. View Transaction History")
            print("6. Exit")

            choice = input("Choose an option (1-6): ")

            if choice == "1":
                if self.check_pin():
                    self.balance_inquiry()
            elif choice == "2":
                if self.check_pin():
                    self.withdraw_cash()
            elif choice == "3":
                if self.check_pin():
                    self.deposit_cash()
            elif choice == "4":
                if self.check_pin():
                    self.change_pin()
            elif choice == "5":
                if self.check_pin():
                    self.view_transaction_history()
            elif choice == "6":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

# Instantiate the ATM simulation and start the main menu
if __name__ == "__main__":
    atm = ATMSimulation()
    atm.main_menu()
