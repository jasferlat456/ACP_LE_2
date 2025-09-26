#For storing student details
class Student:
    def __init__(self, student_id, student_name, email, grades: dict = None, courses: set = None):
        self.id_name = student_id, student_name
        self.email = email
        self.grades = grades if grades is not None else {}
        self.courses = courses if courses is not None else set()

    #use for displaying all information of a student
    def __str__(self):
        student_id, student_name = self.id_name
        grades_info = ", ".join(f"{subj}: {score}" for subj, score in self.grades.items())
        courses_info = ", ".join(self.courses)
        
        gpa = self.calculate_gpa()
        
        return (
            f"Student Record\n"
            f"ID: {student_id}\n"
            f"Name: {student_name}\n"
            f"Email: {self.email}\n"
            f"Grades: {grades_info}\n"
            f"GPA: {gpa:.2f}\n"
            f"Courses: {courses_info}"
        )

    #Calculates the grade all grades then convert into average
    def calculate_gpa(self):
        if not self.grades:
            return 0.0

        total_gpa_points = 0
        num_subjects = 0
        
        for grade in self.grades.values():
            if grade >= 90:
                grade_point = 4.0
            elif grade >= 80:
                grade_point = 3.0
            elif grade >= 70:
                grade_point = 2.0
            elif grade >= 60:
                grade_point = 1.0
            else:
                grade_point = 0.0
                
            total_gpa_points += grade_point
            num_subjects += 1
            
        return round(total_gpa_points / num_subjects, 2) if num_subjects > 0 else 0.0

#Added another student class for record management
class StudentRecords:
    def __init__(self):
        self.students = []
        
    def add_student(self, student_id, student_name, email, grades: dict = None, courses: set = None):
        if self._find_student(student_id):
            return f"Error: Student with ID {student_id} already exists."
            
        new_student = Student(student_id, student_name, email, grades, courses)
        self.students.append(new_student)
        return f"Student added successfully: {student_name} (ID: {student_id})"
    
    #Updating or modifiying students info
    def update_student(self, student_id, email = None, grades: dict = None, courses: set = None):
        student = self._find_student(student_id)
        
        if student:
            if email is not None:
                student.email = email
            if grades is not None:
                student.grades.update(grades)
            if courses is not None:
                student.courses.update(courses)
            return f"Student ID {student_id} updated successfully."
        else:
            return f"Error: Student ID {student_id} not found."
    
    #delete student usuing student id
    def delete_student(self, student_id):
        student_to_delete = self._find_student(student_id)
        
        if student_to_delete:
            self.students.remove(student_to_delete)
            return f"Student deleted successfully: ID {student_id}"
        else:
            return f"Error: Student ID {student_id} not found."
    
    #function for student to enroll a course
    def enroll_course(self, student_id, course):
        student = self._find_student(student_id)
        
        if student:
            student.courses.add(course)
            return f"Student ID {student_id} successfully enrolled in '{course}'."
        else:
            return f"Error: Student ID {student_id} not found."
    
    #Added function to easily find the student
    def _find_student(self, student_id):
        for student in self.students:
            if student.id_name[0] == student_id:
                return student
              
        return None
      
    #Search student using if else statement
    def search_student(self, student_id):
        student = self._find_student(student_id)
        if student:
            return student
        else:
            return f"Error: Student ID {student_id} not found."
    
    #Search function using name(even lower case)
    def search_by_name(self, name):
        matches = []
        search_name_lower = name.lower()
        
        for student in self.students:
            student_name_lower = student.id_name[1].lower()
            
            if search_name_lower in student_name_lower:
                matches.append(student)
                
        if matches:
            return (f"Student named {name} found")
        else:
            return (f"Error: No students found matching the name '{name}'.")

#Printing all the existing information when called
if __name__ == '__main__':
    records = StudentRecords()

    print("Adding Students")
    print(records.add_student(1001, "Jasfer Lat", "jasfer@school.edu", {"Math": 95, "Science": 85}, {"Calculus"}))
    print(records.add_student(1002, "Alicia Keys", "alicia@school.edu"))
    print(records.add_student(1003, "Bobby Brown", "bobby@school.edu", {"English": 70, "Art": 92}))
    print()
    print("Update Student Information")
    print(records.enroll_course(1001, "History"))
    print(records.update_student(1002, email="aliciaj@school.edu", grades={"Biology": 65}))
    print(records.update_student(1003, courses={"ICT", "English"}))
    print()
    print("Search Student by ID")
    print(records.search_student(1001))
    print()
    print("Search Student by Name")
    print(records.search_by_name("jasfer"))
    print(records.search_by_name("ally"))
    print()
    print("Delete Student")
    print(records.delete_student(1002))
    print(records.search_student(1002))
