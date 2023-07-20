# Classes Exercise

class Student:

    def __init__(self, name, age, group="student"):
        self.name = name
        self.age = age
        self.group = group 

    def average(self, number_1, number_2, number_3):
       return ((number_1 + number_2 + number_3) / 3)

Cinnabun = Student("Cinnabunuwu", 22, "1B")

average = Cinnabun.average(22, 84, 11)

print (f"wazzaaaaap. i is class. i so smart. i give you average of 3 numbers you gave me wow: average is: {average}") 


### Budget App
# Goal: “Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. 
# These objects should allow for depositing and withdrawing funds from each category, 
# as well computing category balances and transferring balance amounts between categories”

class Budget:

    def __init__(self, category, budget=0):
        self.budget = budget
        self.category = category
    
    def deposit(self, amount):
        self.budget += amount
        print("Aye well done good sir")

    def withdraw(self, amount):
        if (self.budget - amount < 0):
            print("You\'ve spent too much yarrrrr")
        else:
            self.budget -= amount

   # def transfer(self, amount): #transfer between categories
     #   pass #still workin on this part


foodYUM = Budget(10, "FOODYUM")
clothes = Budget(8, "Clothes")
entertainment = Budget(200, "meaningoflife")

moreFoodMaybe = input("Did ya eat this month? Type \'yes\' or \'no\'")

if moreFoodMaybe == "yes":
     moreFoodYes = int(input("How much did ya spend ya rascal? "))
else:
     pass #workin on here