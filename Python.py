# Python Exercises

word1 = "Good"
word2 = "Day"
word3 = "John"

sentence = word1 + " " + word2 + " " + word3

print(sentence)

# next section - what will this code output?

number1 = input("Enter whole number: ")
number2 = input("Enter decimal number: ")

integer_number = int(number1)
float_number = float(number2)
round_number = int(round(float_number))

print(number1)
print(number2)
print(round_number)

# Enter whole number: 
# Enter decimal number:
# it would be an error cause the string can't be converted to an integer

# Next question - what is this piece of code doing?

# Pet
name = "Pep Guardogiola"
age = 3
bark = True
tweet = False

print("My pet is called", name, ", He is", age, "years old.")
print("Statement:", name, "barks.", bark)
print("Statement:", name, "tweets.", tweet)

# Well, the output is describing the pet and then the guy is talking to his pet
# And the last two inputs would output the booleans 1 for bark and 0 for tweet