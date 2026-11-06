# Create a Bank acount class with attributes ,account_number ,owner_name,and balance.


class BankAccount:

    # Constructor
    def __init__(self, account_number, owner_name, balance):

        # Initialize attributes
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance


# Creating an object
account1 = BankAccount(123456, "Jayendra Kumar", 5000)

# Display account details
print("Account Number:", account1.account_number)
print("Owner Name:", account1.owner_name)
print("Balance:", account1.balance)

# output:
# Account Number: 123456
# Owner Name: Jayendra Kumar
# Balance: 5000
