class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)
class Teacher(Student):
    def __init__(self, name, age, grade, subject):
        super().__init__(name, age, grade)
        self.subject = subject

    def show_teacher(self):
        self.show_info()
        print("Subject:", self.subject)
s1 = Student("Ali", 20, "A")
s1.show_info()

t1 = Teacher("Sara", 30, "Teacher", "Math")
t1.show_teacher()