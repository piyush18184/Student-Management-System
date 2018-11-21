from Course import *
from ListOfCourses import CourseList as c
from ListOfMajors import *
from Course import *
from ListOfStudents import *
from Major import *
from ListOfParticularCourses import *
from Student import *
import sys


if __name__ == '__main__':

    while True:
        print()
        print("1:Student name")
        print("2:Available Courses")
        print("3. Add Courses")
        print("4:Remove Courses")
        print("5. Show Cart")
        print("Press any other key to exit")
        print()
        print("Enter choice:")
        num = int(input())
        print()

        if num == 1:
            print("Student's List from the records:")
            print("Roll Number", "  Student Name","     ", "ID")
            for i in Student.list_students:
                print(i.GetStudentRollNumber(),"    ",i.GetStudentName(),i.GetStudentID())

        elif num == 2:
            print("S.No.", "Course Name", "Course ID", "Course Price")
            c=1
            for i in Courses.list_course:
                print(c,"    ",i.GetCourseName(),"      ",i.GetCourseID(),"    ",i.GetCoursePrice())
                c=c+1

        elif num == 3:
            while True:
                print("Enter the roll number of student whose cart needs to be modified(press 0 to exit):")
                roll=input()
                if int(roll) == 0:
                    break
                else:
                        print("Enter the Course Number to be added")
                        print("Press any other key apart from 1-6 to exit")
                        s=int(input())

                        if s==1:
                            student1.BuyCourse(course1,roll)
                            print("%s" % student1.GetCart().ShowCart())
                            student1.AddCart()
                        elif s==2:
                            student1.BuyCourse(course2,roll)
                            print("%s" % student1.GetCart().ShowCart())
                            student1.AddCart()
                        elif s==3:
                            student1.BuyCourse(course3, roll)
                            print("%s" % student1.GetCart().ShowCart())
                            student1.AddCart()
                        elif s==4:
                            student1.BuyCourse(course4, roll)
                            print("%s" % student1.GetCart().ShowCart())
                            student1.AddCart()
                        elif s==5:
                            student1.BuyCourse(course5, roll)
                            print("%s" % student1.GetCart().ShowCart())
                            student1.AddCart()
                        elif s==6:
                            student1.BuyCourse(course6, roll)
                            print("%s" % student1.GetCart().ShowCart())
                            student1.AddCart()
                        else:
                            print("Invalid Input")
                            break


        elif num== 4:
            while True:
                print("Enter the roll number of student whose cart needs to be removed(press 0 to exit):")
                roll = input()
                if int(roll) == 0:
                    break
                else:
                    print("Enter the Course Number to be removed")
                    print("Press any other key apart from 1-6 to exit")
                    s = int(input())

                    if s == 1:
                        student1.Remove(course1, roll)
                        print("%s" % student1.GetCart().ShowCart())
                        student1.AddCart()
                    elif s == 2:
                        student1.Remove(course2, roll)
                        print("%s" % student1.GetCart().ShowCart())
                        #student1.AddCart()
                    elif s == 3:
                        student1.Remove(course3, roll)
                        print("%s" % student1.GetCart().ShowCart())
                        student1.AddCart()
                    elif s == 4:
                        student1.Remove(course4, roll)
                        print("%s" % student1.GetCart().ShowCart())
                        student1.AddCart()
                    elif s == 5:
                        student1.Remove(course5, roll)
                        print("%s" % student1.GetCart().ShowCart())
                        student1.AddCart()
                    elif s == 6:
                        student1.Remove(course6, roll)
                        print("%s" % student1.GetCart().ShowCart())
                        student1.AddCart()
                    else:
                        print("Invalid Input")
                        break

        elif num==5:
            print(student1.GetCart().ShowCart())

        else:
            sys.exit()
