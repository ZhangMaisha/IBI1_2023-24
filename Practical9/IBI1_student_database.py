#Create a class
class Student:  
    def __init__(self, name, major, code_portfolio_score, group_project_score, exam_score):  
        self.name = name  
        self.major = major  
        self.code_portfolio_score = code_portfolio_score  
        self.group_project_score = group_project_score  
        self.exam_score = exam_score  
  
    def print_details(self):  
        print(f"Name: {self.name}, Major: {self.major}, Code Portfolio Score: {self.code_portfolio_score},Group Project Score: {self.group_project_score}, Exam Score: {self.exam_score}")  


# Example usage  
student = Student("A", "BMI", 85, 90, 78)  
student.print_details()  

name = input(" Please enter the student's name: ")
major = input(" Please enter student major: ")
code_portfolio_score = float(input(" Please enter the student's code portfolio score: "))
group_project_score = float(input(" Please enter the student's group project score: "))
exam_score = float(input(" Please enter the student's test score: "))

student = Student(name, major, code_portfolio_score, group_project_score, exam_score)
student.print_details()