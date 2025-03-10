class Student:
    def __init__(self, name, age=None, grade=None):
        self.name = name
        self.age = age
        self.grade = grade


student_1 = Student("Oleksandr")
student_2 = Student("Dmytrii", 9)
student_3 = Student("Nadiia", grade="A")
student_4 = Student("Jimm", 30, "B")
