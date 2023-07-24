#numberlist = [3, 56, 78, 55, 39, 99, 1, 13]

#for poopie in range(4):
   # print(poopie)

#len as leon

#import random

#def i_like_to_roll_it_roll_it():
    #return(random.randint(1,6))

def factorial(x: int) -> int:
    '''
    factorial(x): Creates factorial function that returns the product of all ints from 1 to x.
    '''
    result = 1
    for i in range(2, x + 1):
        result *= i
        return result
    
if __name__ == '__main__':
    print(factorial(3))
    print (factorial(5))
    print (factorial(10)) # prints 100 (10*10)

# If you use ''' insert info here ''' you can declare a string for a particular function
# so the string will be generated alongside the function if you do help(factorial)

#python3 -m pydoc -w DOCNAME (writes html but only works in normal shell)