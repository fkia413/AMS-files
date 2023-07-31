
# Debugging woopie let me bring my mosquito repellent

# Exercise 1 (static) 

user_funds = 10.31
item_price = price["Burger"] #price is not defined

if item_price < user_funds: #user_funds is a float while item_price is a string so it's not gonna work mate
    Print("You have enough money!") #print needs to be lower case
if item_price = user_funds: #they need to put == not =
    print("You have the precise amount of money")
if item_price < user_funds:
    print(Sorry you don't have enough money) 
# the apostrophe messes up the line and there needs to be quotation marks

#Exercise 2 (static)

def product(n):
    total == 1 #they should use = instead
    for n in n: #n in n doesn't make sense, should be for n in product
       total *= i # i isn't defined
return total

print(product([4,4,5])) #they need to add 3 parameters in product() since it has 3 here

# Exercise 3 (dynamic debugging yaey) so im gonna use pdb for dis one ye

import pdb
pdb.set_trace()

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0: # Needed to add == instead of -
                return False
            return True

#Test the is_prime function with 2, 3, 4, 5, 6, 7, 15, 20 & 25

# Exercise 4 (dynamic debugging)

item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]

n = 0

while n < 5:
    for i in item_list:
        print(i) # list needed to be int not str so only left [i] instead of item_list[i]
        n += 5 # added this line to stop the unlooping loop from destroying my pc

print(item_list[4]) # missing parenthesis so added them, and changed 5 to 4 cause otherwise it would print 6 times

