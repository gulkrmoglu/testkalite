from studentclass import Student
from teacherclass import Teacher

student_list=[]
teacher_list=[]

def addStudent(name,studentNumber,department):
    newStudent = Student(name,studentNumber,department)
    student_list.append(newStudent)

def addTeacher(name,teacherId,department):
    newTeacher = Teacher(name,teacherId,department)
    teacher_list.append(newTeacher)

def returnStudentList():
    for student in student_list:
        print(student.studentInfo())

def returnTeacherList():
    for teacher in teacher_list:
        print(teacher.teacherInfo())

addStudent("Emine",200,"Matematik")
addStudent("Gül",350,"Gazetecilik")

addTeacher("İrem",500,"Tobeto")
addTeacher("Mustafa",450,"Tobeto")

returnStudentList()
returnTeacherList()