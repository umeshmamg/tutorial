import json
import os

# Function to load account data from a JSON file
def load_accounts():
    if os.path.exists("accounts.json"):
        with open("accounts.json", "r") as file:
            accounts = json.load(file)
    else:
        accounts = {}
    return accounts

# Function to save account data to a JSON file
def save_accounts(accounts):
    with open("accounts.json", "w") as file:
        json.dump(accounts, file)

# Function to create a new bank account
def create_account(accounts):
    account_number = input("Enter account number: ")
    if account_number in accounts:
        print("Account already exists.")
    else:
        name = input("Enter account holder's name: ")
        balance = float(input("Enter initial balance: "))
        accounts[account_number] = {"name": name, "balance": balance}
        print("Account created successfully.")

# Function to deposit money into an account
def deposit(accounts):
    account_number = input("Enter account number: ")
    if account_number in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[account_number]["balance"] += amount
        print("Deposit successful.")
    else:
        print("Account not found.")

# Function to withdraw money from an account
def withdraw(accounts):
    account_number = input("Enter account number: ")
    if account_number in accounts:
        amount = float(input("Enter amount to withdraw: "))
        if accounts[account_number]["balance"] >= amount:
            accounts[account_number]["balance"] -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found.")

# Function to check account balance
def check_balance(accounts):
    account_number = input("Enter account number: ")
    if account_number in accounts:
        print(f"Current balance: {accounts[account_number]['balance']}")
    else:
        print("Account not found.")

# Function to view account details
def view_account_details(accounts):
    account_number = input("Enter account number: ")
    if account_number in accounts:
        print(f"Account Number: {account_number}")
        print(f"Account Holder's Name: {accounts[account_number]['name']}")
        print(f"Current Balance: {accounts[account_number]['balance']}")
    else:
        print("Account not found.")

# Main function to run the application
def main():
    accounts = load_accounts()

    while True:
        print("\n--- Bank Management System ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. View Account Details")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit(accounts)
        elif choice == "3":
            withdraw(accounts)
        elif choice == "4":
            check_balance(accounts)
        elif choice == "5":
            view_account_details(accounts)
        elif choice == "6":
            save_accounts(accounts)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
