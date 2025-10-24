
# %%

class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def display_info(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):

    def __init__(self, name: str, age: int, student_id: str, grades: list[int]):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = grades
    
    def calculate_average(self) :
        total_sum = 0
        for item in self.grades:
            total_sum += item
        return float(total_sum) / len(self.grades)
     
    def display_info(self) -> str:
        return f"{super().display_info()}, Grades: {self.grades}, Average: {self.calculate_average()}"
    
class Teacher(Person):

    def __init__(self, name: str, age: int, employee_id: str, subject: str ):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subect = subject
    
    def display_info(self) -> str:
        return f"{super().display_info()}, Employee Id: {self.employee_id}, Subject: {self.subect}"


sample_student = Student("Tyrone", 18, "163920", [75,90,89,89,90])
sample_teacher = Teacher("Dela Cruz", 30, "3123123", "MATH")

perzon = [sample_student, sample_teacher]

for i, item in enumerate(perzon):
    print(f"Perzon {i}: {item.display_info()}")
# %%
