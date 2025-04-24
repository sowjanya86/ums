class Person:
    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name

class Student(Person):
    def __init__(self, rollno, name, branch):
        super().__init__(rollno, name)
        self.branch = branch

class Teacher(Person):
    def __init__(self, rollno, name, subject):
        super().__init__(rollno, name)
        self.subject = subject

class College:
    def __init__(self, cname):
        self.cname = cname
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def search_student(self, rollno):
        for student in self.students:
            if student.rollno == rollno:
                return student
        return None

    def search_teacher(self, rollno):
        for teacher in self.teachers:
            if teacher.rollno == rollno:
                return teacher
        return None

colleges = []

while True:
    print("Choose the Required option: ")
    print("1. Create College.")
    print("2. Add Student.")
    print("3. Add Teacher.")
    print("4. Display Students.")
    print("5. Display Teachers.")
    print("6. Search Student by Roll Number.")
    print("7. Search Teacher by Roll Number.")
    print("8. Exit.")
    x = int(input("Enter your Option: "))

    if x == 1:
        clgname = input("Enter College Name: ")
        if any(c.cname == clgname for c in colleges):
            print("\nCollege Already Exists!\n")
        else:
            colleges.append(College(clgname))
            print("\nCollege Added Successfully\n")
    
    elif x in [2, 3]:
        clgname = input("Enter College Name: ")
        clg = next((c for c in colleges if c.cname == clgname), None)
        
        if clg:
            rollno = input("Enter Roll No: ")
            name = input("Enter Name: ")
            if x == 2:
                branch = input("Enter Student Branch: ")
                clg.add_student(Student(rollno, name, branch))
                print("\nStudent Added Successfully\n")
            else:
                subject = input("Enter Subject: ")
                clg.add_teacher(Teacher(rollno, name, subject))
                print("\nTeacher Added Successfully\n")
        else:
            print("\nCollege Does Not Exist!\n")
    
    elif x in [4, 5]:
        clgname = input("Enter College Name: ")
        clg = next((c for c in colleges if c.cname == clgname), None)
        
        if clg:
            details = clg.students if x == 4 else clg.teachers
            entity = "Student" if x == 4 else "Teacher"
            
            if details:
                for i, person in enumerate(details, 1):
                    print(f"{entity} {i}:")
                    print(f"Roll Number: {person.rollno}")
                    print(f"Name: {person.name}")
                    print(f"{'Branch' if x == 4 else 'Subject'}: {getattr(person, 'branch' if x == 4 else 'subject')}")
                    print()
            else:
                print(f"\nNo {entity}s Found!\n")
        else:
            print("\nCollege Does Not Exist!\n")
    
    elif x in [6, 7]:
        clgname = input("Enter College Name: ")
        clg = next((c for c in colleges if c.cname == clgname), None)
        
        if clg:
            rollno = input("Enter Roll Number: ")
            person = clg.search_student(rollno) if x == 6 else clg.search_teacher(rollno)
            entity = "Student" if x == 6 else "Teacher"
            
            if person:
                print(f"\n{entity} Details:")
                print(f"Roll Number: {person.rollno}")
                print(f"Name: {person.name}")
                print(f"{'Branch' if x == 6 else 'Subject'}: {getattr(person, 'branch' if x == 6 else 'subject')}")
                print()
            else:
                print(f"\n{entity} Not Found!\n")
        else:
            print("\nCollege Does Not Exist!\n")
    
    elif x == 8:
        break
    else:
        print("\nChoose a Correct Option!\n")
