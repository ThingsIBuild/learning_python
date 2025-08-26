
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks


    def student_info(self):
        return f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}"

    def has_passed(self):
        return self.marks > 40

    def is_eligible(self):
        if self.age >= 18 :
            return f"{self.name} is eligible"
        else:
            return f"{self.name} is not eligible"
        

student1 = Student("Alice", 20, 85)

print(student1.student_info()) 
print(student1.has_passed())
print(student1.is_eligible())