class Student:
    def __init__(self, firstname,course,gender):
        self.firstname = firstname
        self.course = course
        self.gender = gender


    def study(self):
        print(self.firstname, "is studying")

student1 = Student("Sam","CyberSecurity","Male")
student1.study()

student2 = Student("Neemah","Datascience","Female")
student2.study()

student3 = Student("Makena","MIT","Female")
