# Functions Exercise

def finalgrade(name, homework_score, assessment_score, final_exam_score, letter_grade):
    return f"Wazzup {name}, your final ICT grade as a percentage is {calculation}%. Your grade is {letter_grade}"

name = input("State your name muahahaha: ")
homework_score = int(input("State your homework score: "))
assessment_score = int(input("State your assessment score: "))
final_exam_score = int(input("And now...give me your final exam score: "))

calculation = int((homework_score + assessment_score + final_exam_score)/175*100)
if calculation >= 80:
        letter_grade = "A for Awesome"
elif calculation >= 70:
        letter_grade = "B for you da Best"
elif calculation >= 60:
        letter_grade = "C for Clever"
elif calculation >= 50:
        letter_grade = "D for Dumbo"
elif calculation >= 40:
        letter_grade = "E for Elon Musk-level of smartness. I have faith that you'll build us a spaceship to Mars."

print(finalgrade(name, homework_score, assessment_score, final_exam_score, letter_grade))

# W3 Functions Practice

#Question 1 - Write a Python function to find the maximum of 3 numbers:

def maximum(number_1, number_2, number_3, max):
       return f"Hoi. i is function. i so smart. i give you maximum of 3 numbers you gave me wow: maximum is {max}!!!"

number_1 = int(input("Gimme a number: "))
number_2 = int(input("Gimme more number ples: "))
number_3 = int(input("I WANT MORE NUMBER: "))
max = max(number_1, number_2, number_3) 

print(maximum(number_1, number_2, number_3, max))