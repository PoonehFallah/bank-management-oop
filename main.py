#Account
class Account:
    def __init__(self, name, account_id, balance):
        self.name = name
        self.account_id = account_id
        self.balance = balance
        self.transactions = ["Account Created"]

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit : +{amount:,}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdraw : -{amount:,}")
            return True
        return False

    def show_balance(self):
        return self.balance

    def show_history(self):
        if len(self.transactions) == 0:
            print("No Transactions")
        else:
            print("------ Transaction History ------")
            for transaction in self.transactions:
                print(transaction)
#Bank
class Bank:
    def __init__(self):
        self.accounts = []
        self.next_id = 1000

    def create_account(self, name, balance):
        account = Account(name, self.next_id, balance)
        self.accounts.append(account)
        self.next_id += 1
        return account

    def login(self, account_id):
        for account in self.accounts:
            if account.account_id == account_id:
                return account
        return None

    def transfer(self, sender, receiver_id, amount):
        receiver = self.login(receiver_id)
        if receiver == None:
            return False, "Account Not Found"

        if sender.withdraw(amount):
            receiver.deposit(amount)
            sender.transactions.append(f"Transfer To {receiver.account_id} : -{amount:,}")
            receiver.transactions.append(f"Transfer From {sender.account_id} : +{amount:,}")
            return True, "Transfer Successful"
        return False, "Insufficient Balance"

    def change_name(self, account, new_name):
        account.name = new_name
        account.transactions.append("Name Changed")

    def delete_account(self, account):
        if account in self.accounts:
            self.accounts.remove(account)
            return True
        return False
#Main
bank = Bank()
while True:
    print("------ BANK ------")
    print("1.Create Account")
    print("2.Login")
    print("3.Exit")
    choose = input("Choose: ")
    if choose == "1":
        name = input("Enter Name: ")
        balance = int(input("Enter Balance: "))
        account = bank.create_account(name, balance)
        print("Account Created Successfully")
        print("Account ID:", account.account_id)

    elif choose == "2":
        login_id = int(input("Enter Account ID: "))
        account = bank.login(login_id)

        if account:
            print("Login Successful")
            print("Welcome", account.name)

            while True:
                print("------ MENU ------")
                print("1.Deposit")
                print("2.Withdraw")
                print("3.Transfer")
                print("4.Show Balance")
                print("5.Transaction History")
                print("6.Change Name")
                print("7.Delete Account")
                print("8.Logout")
                choice = input("Choose: ")

                if choice == "1":
                    amount = int(input("Amount: "))
                    account.deposit(amount)
                    print("Deposit Successful")

                elif choice == "2":
                    amount = int(input("Amount: "))

                    if account.withdraw(amount):
                        print("Withdraw Successful")
                    else:
                        print("Insufficient Balance")

                elif choice == "3":
                    receiver_id = int(input("Receiver Account ID: "))
                    amount = int(input("Amount: "))

                    success, message = bank.transfer(account,receiver_id,amount)
                    print(message)

                elif choice == "4":
                    print("Balance:", f"{account.balance:,}")

                elif choice == "5":
                    account.show_history()

                elif choice == "6":
                    new_name = input("New Name: ")
                    bank.change_name(account, new_name)
                    print("Name Changed Successfully")

                elif choice == "7":
                    if bank.delete_account(account):
                        print("Account Deleted")
                        break

                elif choice == "8":
                    print("Logout Successful")
                    break
                else:
                    print("Invalid Choice")
        else:
            print("Account Not Found")
    elif choose == "3":
        print("Good Bye")
        break
    else:
        print("Invalid Choice")