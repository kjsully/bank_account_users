class BankAccount:

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance > 0:
            self.balance -= amount
        else:
            print("insufficient funds: charging a $5 fee haha")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance - self.balance * self.int_rate
        return self



class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self 

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self 
        
    def display_user_balance(self):
        self.account.display_account_info()
        return self


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
kyle = User('Kyle Sullivan', 'kyle@python.com')

kyle.make_deposit(50)
kyle.display_user_balance()