# Users stored in a dictionary: username as key, password as value, 
#key value mindset
# I stored the info in a dictionnary

users = {
    "Antoine": "pass123",
    "Onome": "secret",
    "Sean": "hello2025"
}

# I sartt with a balance
balance = 25000

print("Welcome to National Bank ATM\n")

# Login system
#Whatever the user types it gets stored in the variable
username = input("Enter username: ")

#Chacking if username is in the dictionary
if username in users:
    password = input("Enter password: ")
    if password == users[username]:
        print("Login successful!\n")
        
        # Menu after login
        #f enables me access the variable balance within the string
        print(f"Current balance: ${balance}\n")
        print("Choose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Invest")
        print("5. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            amount = float(input("What is the amount to deposit? "))
            balance += amount
            print(f"\nDeposited ${amount}. New balance: ${balance}")
            print("\nKeep growing that balance, Bravo!")

    else:
        print("Incorrect password.")
else:
    print("User does not exist.")
