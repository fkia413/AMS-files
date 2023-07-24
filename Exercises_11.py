class Student:
    '''Student: declares a class called Student.'''

    def __init__(self, name, age, group="student"):
        self.name = name
        self.age = age
        self.group = group 

    def average(self, number_1, number_2, number_3):
       return ((number_1 + number_2 + number_3) / 3)

if __name__ == '__main__':
    print(Student("Cinnabunuwu", 22, "1B"))
