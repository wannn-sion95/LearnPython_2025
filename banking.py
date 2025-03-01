class bankAccount():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}\nNew Balance: {self.__balance}")
    

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}\nNew Balance: {self.__balance}")
        else:
            print("Invalid amount or insufficient balance.")

    def get_balance(self):
        return self.__balance

account = bankAccount("Rayna", 1000000)
account.deposit(500000)
account.withdraw(200000)
print(f"Informasi Akun Bank: {account.get_balance()}")
