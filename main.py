class BankAccount:
    def __init__(self, name, accountNumber, accountType, balance=0):
        try:
            self.name = name
            self.accountType = accountType
            self.balance = balance
            self.accountNumber = accountNumber
            self.filename = f"{self.accountNumber}_{self.accountType}_{self.name}.txt"

            with open(self.filename, 'w') as f:
                f.write(
                    f"Account Statement for {self.name}, {self.accountType}, Account Number: {self.accountNumber}\n")
                f.write(f"Initial balance: {self.balance}\n")

        except Exception as e:
            print("Error creating account:", e)

    def deposit(self, money):
        try:
            if money > 0:
                self.balance += money
                with open(self.filename, 'a') as f:
                    f.write(f"Deposit: {money}, New balance: {self.balance}\n")
                print(f"Added {money} to the account under the name of: {self.getAccountName()}")
            else:
                print("Deposit amount must be positive.")
        except Exception as e:
            print("Error during deposit:", e)

    def withdraw(self, money):
        try:
            if 0 < money <= self.balance:
                self.balance -= money
                with open(self.filename, 'a') as f:
                    f.write(f"Withdrawal: {money}, New balance: {self.balance}\n")
                print(f"Withdrew {money} from the account under the name of: {self.getAccountName()}")
            else:
                print("Invalid withdrawal amount. Check if the amount is positive and less than or equal to balance.")
        except Exception as e:
            print("Error during withdrawal:", e)

    def checkBalance(self):
        print(f"Current balance is: {self.balance}")

    def getAccountType(self):
        return self.accountType

    def getAccountNum(self):
        return self.accountNumber

    def getAccountName(self):
        return self.name

    def transactionHistory(self):
        try:
            with open(self.filename, 'r') as file:
                print(file.read())
        except Exception as e:
            print("Error reading transaction history:", e)


def createAcctNum():
    while True:
        num = input("Enter an 8-digit number: ")
        if num.isdigit() and len(num) == 8:
            return int(num)
        else:
            print("Invalid input. Please enter exactly 8 digits.")


def createAcctType():
    while True:
        account_type = input("Enter account type (chequing/savings): ").lower()
        if account_type in ['chequing', 'savings']:
            return account_type
        else:
            print("Invalid input. Please enter either 'chequing' or 'savings'.")


def main():
    account1 = BankAccount("JohnDoe", createAcctNum(), createAcctType())
    account2 = BankAccount("JaneDoe", createAcctNum(), createAcctType(), 100)

    account1.deposit(50)
    account1.withdraw(20)
    account1.checkBalance()

    account2.deposit(200)
    account2.withdraw(50)
    account2.checkBalance()

    print(f"Account 1 ID: {account1.getAccountNum()}")
    print(f"Account 1 Username: {account1.getAccountName()}")
    print(f"Account 1 Type: {account1.getAccountType()}")
    account1.checkBalance()
    print("Account 1 Transaction History:")
    account1.transactionHistory()

    print(f"\nAccount 2 ID: {account2.getAccountNum()}")
    print(f"Account 2 Username: {account2.getAccountName()}")
    print(f"Account 2 Type: {account2.getAccountType()}")
    account2.checkBalance()
    print("Account 2 Transaction History:")
    account2.transactionHistory()


main()
