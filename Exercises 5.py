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