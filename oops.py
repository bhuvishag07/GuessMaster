# 1. Student class: name, roll, marks → compute average
print("\n--- 1. Student Class ---")
class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks  # list of marks

    def average(self):
        return sum(self.marks) / len(self.marks)


# Example
s = Student("Bhuvisha", 1, [90, 95, 88])
print("Name:", s.name)
print("Roll:", s.roll)
print("Average Marks:", s.average())



# 2. BankAccount class: deposit, withdraw, balance check
print("\n--- 2. BankAccount Class ---")
class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def check_balance(self):
        print("Current Balance:", self.balance)


# Example
acc = BankAccount("Amit", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.check_balance()



# 3. Car class with brand, model, and drive() method
print("\n--- 3. Car Class ---")
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(self.brand, self.model, "is now driving...")


# Example
c = Car("Toyota", "Fortuner")
c.drive()



# 4. Restaurant class: menu stored in dict, print bill
print("\n--- 4. Restaurant Class ---")
class Restaurant:
    def __init__(self):
        self.menu = {}  # item → price

    def add_item(self, item, price):
        self.menu[item] = price

    def bill(self, orders):
        total = 0
        for item in orders:
            if item in self.menu:
                total += self.menu[item]
            else:
                print(item, "not available!")
        print("Total Bill =", total)


# Example
r = Restaurant()
r.add_item("Pizza", 200)
r.add_item("Burger", 100)
r.add_item("Pasta", 150)
r.bill(["Pizza", "Pasta"])



# 5. User class with private password + login validation
print("\n--- 5. User Login Class ---")
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password   # private variable

    def login(self, username, password):
        if self.username == username and self.__password == password:
            print("Login Successful!")
        else:
            print("Invalid Credentials")


# Example
u = User("bhuvi", "12345")
u.login("bhuvi", "12345")
u.login("bhuvi", "wrongpass")
