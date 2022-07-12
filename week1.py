'''Create a Python scriptwith following criteria:
a)  Create a class Name Students with following attributes:

Student ID, Student First Name, Student Last Name, Course, Year, GPA, University, Email, Mobile.

Create at least 3 instances for the above class.

b)  Use appropriate types of Attributes.

Use appropriate types of Properties.
Use appropriate types of Methods.
Create Email based on First Name and Last Name of the Student. (NOTE: If we modify FirstName or Last Name it has to reflect in Email.) '''

def main():
    print("Welcome to the Student Database")
    print("Please enter the following information:")
    student1 = Student("1", "John", "Doe", "CS", "1", "3.5", "UCLA")
    student2 = Student("2", "Jane", "Doe", "CS", "1", "3.5", "UCLA")
    student3 = Student("3", "Joe", "Doe", "CS", "1", "3.5", "UCLA")
    student1.print_student()
    student2.print_student()
    student3.print_student()

class Student:
    def __init__(self, id, first_name, last_name, course, year, gpa, university):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.course = course
        self.year = year
        self.gpa = gpa
        self.university = university
        self.email = first_name + "." + last_name + "@" + university + ".edu"
        self.mobile = "(" + id + ")" + first_name[0] + last_name[0] + "-" + last_name[1] + last_name[2]
    def print_student(self):
        print("Student ID: " + self.id)
        print("Student First Name: " + self.first_name)
        print("Student Last Name: " + self.last_name)
        print("Student Course: " + self.course)
        print("Student Year: " + self.year)
        print("Student GPA: " + self.gpa)
        print("Student University: " + self.university)
        print("Student Email: " + self.email)
        print("Student Mobile: " + self.mobile)

main()
