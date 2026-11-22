import random
from datetime import datetime


# ============================================================
# PARENT CLASS
# ============================================================

class BankAccount:

    def __init__(self, username, password, account_number):

        self.username = username
        self.__password = password
        self.__balance = 0
        self.account_number = account_number
        self.transactions = []

    # GET PASSWORD
    def get_password(self):
        return self.__password

    # GET BALANCE
    def get_balance(self):
        return self.__balance

    # CREDIT / DEPOSIT
    def credit(self, amount):

        if amount > 0:

            self.__balance += amount

            transaction = {
                "type": "Credit",
                "amount": amount,
                "date": datetime.now()
            }

            self.transactions.append(transaction)

            print("\nAmount Credited Successfully")
            print("Credited Amount :", amount)
            print("Current Balance :", self.__balance)

        else:
            print("\nInvalid Amount")

    # DEBIT / WITHDRAW
    def debit(self, amount):

        if amount <= 0:
            print("\nInvalid Amount")

        elif amount > self.__balance:
            print("\nInsufficient Balance")

        else:

            self.__balance -= amount

            transaction = {
                "type": "Debit",
                "amount": amount,
                "date": datetime.now()
            }

            self.transactions.append(transaction)

            print("\nAmount Debited Successfully")
            print("Debited Amount :", amount)
            print("Current Balance :", self.__balance)

    # BALANCE ENQUIRY
    def balance_enquiry(self):

        print("\n================================")
        print("        BALANCE ENQUIRY")
        print("================================")

        print("Account Number :", self.account_number)
        print("Account Holder :", self.username)
        print("Available Balance :", self.__balance)

    # MINI STATEMENT
    def mini_statement(self):

        print("\n================================")
        print("         MINI STATEMENT")
        print("================================")

        print("Account Number :", self.account_number)
        print("Account Holder :", self.username)

        if len(self.transactions) == 0:

            print("\nNo Transactions Available")

        else:

            print("\n--------------------------------")
            print("Type\t\tAmount\t\tDate")
            print("--------------------------------")

            for transaction in self.transactions[-5:]:

                print(
                    transaction["type"],
                    "\t\t",
                    transaction["amount"],
                    "\t\t",
                    transaction["date"].strftime("%d-%m-%Y %H:%M:%S")
                )

        print("--------------------------------")
        print("Available Balance :", self.__balance)


# ============================================================
# CHILD CLASS
# ============================================================

class SavingsAccount(BankAccount):

    def __init__(self, username, password, account_number):

        super().__init__(
            username,
            password,
            account_number
        )

        self.account_type = "Savings Account"

    # ACCOUNT DETAILS
    def account_details(self):

        print("\n================================")
        print("         ACCOUNT DETAILS")
        print("================================")

        print("Account Holder :", self.username)
        print("Account Number :", self.account_number)
        print("Account Type   :", self.account_type)
        print("Balance        :", self.get_balance())


# ============================================================
# BANK CLASS
# ============================================================

class Bank:

    def __init__(self):

        self.accounts = {}

    # GENERATE UNIQUE ACCOUNT NUMBER
    def generate_account_number(self):

        while True:

            account_number = random.randint(
                100000000,
                999999999
            )

            duplicate = False

            for account in self.accounts.values():

                if account.account_number == account_number:

                    duplicate = True
                    break

            if duplicate == False:

                return account_number

    # CREATE ACCOUNT
    def create_account(self):

        print("\n================================")
        print("        CREATE ACCOUNT")
        print("================================")

        username = input("Enter Username : ")

        if username in self.accounts:

            print("\nUsername Already Exists")
            return

        password = input("Enter Password : ")

        account_number = self.generate_account_number()

        account = SavingsAccount(
            username,
            password,
            account_number
        )

        self.accounts[username] = account

        print("\nAccount Created Successfully")

        print("--------------------------------")
        print("Username       :", username)
        print("Account Number :", account_number)
        print("Account Type   :", account.account_type)
        print("--------------------------------")

    # LOGIN
    def login(self):

        print("\n================================")
        print("             LOGIN")
        print("================================")

        username = input("Enter Username : ")
        password = input("Enter Password : ")

        if username in self.accounts:

            account = self.accounts[username]

            if account.get_password() == password:

                print("\nLogin Successful")
                print("Welcome,", username)

                self.user_menu(account)

            else:

                print("\nIncorrect Password")

        else:

            print("\nAccount Does Not Exist")

    # USER MENU
    def user_menu(self, account):

        while True:

            print("\n================================")
            print("        BANK ACCOUNT MENU")
            print("================================")

            print("1. Credit")
            print("2. Debit")
            print("3. Balance Enquiry")
            print("4. Mini Statement")
            print("5. Account Details")
            print("6. Logout")

            choice = input("\nEnter Your Choice : ")

            # CREDIT
            if choice == "1":

                try:

                    amount = float(
                        input("Enter Credit Amount : ")
                    )

                    account.credit(amount)

                except ValueError:

                    print("\nPlease Enter Valid Amount")

            # DEBIT
            elif choice == "2":

                try:

                    amount = float(
                        input("Enter Debit Amount : ")
                    )

                    account.debit(amount)

                except ValueError:

                    print("\nPlease Enter Valid Amount")

            # BALANCE ENQUIRY
            elif choice == "3":

                account.balance_enquiry()

            # MINI STATEMENT
            elif choice == "4":

                account.mini_statement()

            # ACCOUNT DETAILS
            elif choice == "5":

                account.account_details()

            # LOGOUT
            elif choice == "6":

                print("\nLogout Successful")
                break

            else:

                print("\nInvalid Choice")

    # MAIN BANK MENU
    def start(self):

        while True:

            print("\n================================")
            print("      BANK MANAGEMENT SYSTEM")
            print("================================")

            print("1. Create Account")
            print("2. Login")
            print("3. Exit")

            choice = input("\nEnter Your Choice : ")

            # CREATE ACCOUNT
            if choice == "1":

                self.create_account()

            # LOGIN
            elif choice == "2":

                self.login()

            # EXIT
            elif choice == "3":

                print("\nThank You For Using Our Bank")
                print("Application Closed")

                break

            else:

                print("\nInvalid Choice")


# ============================================================
# PROGRAM STARTING POINT
# ============================================================

bank = Bank()
bank.start()