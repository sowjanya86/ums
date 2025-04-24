This is a simple command-line-based Python application to manage colleges, students, and teachers. The program allows users to create colleges, add students and teachers, view their details, and search for individuals by roll number.
The application allows you to:
Create multiple colleges
Add students and teachers to specific colleges
Display all students or teachers of a college
Search for a student or teacher by roll number
Store all data in memory during execution (data is lost after the program ends)
The code includes the following classes:
Person: Base class with roll number and name
Student: Inherits from Person, adds branch
Teacher: Inherits from Person, adds subject
College: Contains name, and lists of students and teachers. Supports adding and searching individuals
You'll see a menu with options:
1. Create College
2. Add Student
3. Add Teacher
4. Display Students
5. Display Teachers
6. Search Student by Roll Number
7. Search Teacher by Roll Number
8. Exit
 
 For example, you can:
Create a college named "ABC University"
Add a student named John Doe with roll number 101 and branch CSE
Add a teacher named Dr. Smith with roll number T01 and subject Mathematics
Display all students or teachers from "ABC University"
Search for a specific student or teacher using their roll number









