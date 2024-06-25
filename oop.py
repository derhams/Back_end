# ##encapsulation
# class Alpha:

#     def __init__(self):
#         self._a = 2.  # Protected member ‘a’
#         self.__b = 2.  # Private member ‘b’

# ## POLYMORPHISM
# string = "poly"
# num = 7
# sequence = [1,2,3]
# new_str = string * 3
# new_num = 7 * 3
# new_sequence = sequence * 3

# print(new_str, new_num, new_sequence)

# ##INHERITANCE

# class Parent:
#     Members of the parent class

# class Child(Parent):
#     Inherited members from parent class
#     Additional members of the child class

# class Myclass:
#     a = 5
#     def hello(self):
#         print('hello')

# myc = Myclass()
# print(myc.a)
# print(myc.hello())

# ####
# class House:
#     '''
#     This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
#     '''
#     num_rooms = 5
#     bathrooms = 2
#     def cost_evaluation(self, rate):
#         # Functionality to calculate the costs from the area of the house
#         cost = rate * self.num_rooms
#         return cost

# house = House()
# print(house.num_rooms)
# print(House.num_rooms)

# house.num_rooms = 7
# print(house.num_rooms)
# print(House.cost_evaluation(house, 10))

# House.num_rooms = 7
# print(house.num_rooms)
# print(House.num_rooms)

######
# class Recipe():
#     def __init__(self, dish, items, time) -> None:
#         self.dish = dish
#         self.items = items
#         self.time = time

#     def contents(self):
#         print('The ' + str(self.dish) + ' has ' + str(self.items) + ' and takes ' + str(self.time) + ' Minutes to prepare')

# pizza = Recipe('Pizza', ['cheese', 'bread', 'tomatoes'], 45)
# pasta = Recipe('Pasta', ['penne', 'sauce'], 55)

# print(pizza.contents())
# print(pasta.contents())

# class Payslip:
#     def __init__(self, name, payment, amount) -> None:
#         self.name = name
#         self.payment = payment
#         self.amount = amount

#     def pay(self):
#         self.payment = 'yes'

#     def status(self):
#         if self.payment == 'yes':
#             return self.name + ' is paid ' + str(self.amount)
#         else:
#             return self.name + ' is not yet paid.'
        
# dera = Payslip('Dera', 'yes', 40000)
# ugo = Payslip('Ugo', 'no', 40000)

# print(dera.status(),'\n', ugo.status())
# ugo.pay()
# print('Later that day... ', ugo.status())

#### INHERITANCE
# class Employees:
#     def __init__(self, name, last) -> None:
#         self.name = name
#         self.last = last

# class Supervisors(Employees):
#     def __init__(self, name, last, password) -> None:
#         super().__init__(name, last)
#         self.password = password

# class Chefs(Employees):
#     def leave_request(self, days):
#         return 'May I take a leave for ' + str(days) + ' days'
    
# dera = Supervisors('Dera', 'D', 'life')
# ugo = Chefs('Ugo', 'O')

# print(ugo.leave_request(5))
# print(dera.password)

#######
# Import ABC and abstractmethod from the module abc (which stands for abstract base classes)
from abc import ABC, abstractmethod

# Class Bank
class Bank(ABC):
    """ An abstract bank class

    [IMPLEMENT ME]
        1. This class must derive from class ABC
        2. Write a basicinfo() function that prints out "This is a generic bank" and
           returns the string "Generic bank: 0" 
        3. Define a second function called withdraw and keep it empty by
           adding the `pass` keyword under it. Make this function abstract by
           adding an '@abstractmethod' tag right above the function declaration.
    """
    
    def basicinfo(self):
        print("This is a generic bank")
        return "Generic bank: 0"
    
    @abstractmethod
    def withdraw(self, amount):
        pass

# Class Swiss
class Swiss(Bank):
    """ A specific type of bank than derives from class Bank

    [IMPLEMENT ME]
        1. This class must derive from class Bank
        2. Create a constructor for this class that initializes a class
           variable `bal` to 1000
        3. Implement the basicinfo() function so that it prints "This is the 
           Swiss Bank" and returns a string with "Swiss Bank: " (don't forget
           the space after the colon) followed by the current bank balance.

           For example, if self.bal = 80, then it would return "Swiss Bank: 80"

        4. Implement withdraw so that it takes one argument (in addition to
           self) that is an integer which represents the amount to be withdrawn
           from the bank. Deduct the withdrawn amount from the bank bal, print 
           the withdrawn amount ("Withdrawn amount: {amount}"), print the new
           balance ("New Balance: {self.bal}"), and return the new balance.

           Note: Make sure to verify that there is enough money to withdraw!  
                 If amount is greater than balance, then do not deduct any 
                 money from the class variable `bal`. Instead, print a 
                 statement saying `"Insufficient funds"`, and return the 
                 original account balance instead.
    """
    
    def __init__(self):
        self.bal = 1000

    def basicinfo(self):
        print("This is the Swiss Bank")
        return f"Swiss Bank: {self.bal}"

    def withdraw(self, amount):
        if amount > self.bal:
            print("Insufficient funds")
            return self.bal
        else:
            self.bal -= amount
            print(f"Withdrawn amount: {amount}")
            print(f"New Balance: {self.bal}")
            return self.bal

# Driver Code
def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)

if __name__ == "__main__":
    main()

