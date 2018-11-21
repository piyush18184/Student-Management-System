from Cart import *
from Course import *

class Student():
    list_students = [];
    list_selectedcourse = [];
    def __init__(self, s_id, s_name, m_id):
        self.s_id = s_id
        self.s_name = s_name
        self.m_id = m_id
        self.__cartlist = {}
        self.__cartlist[0] = Cart()
        self.list_students.append(self)
        self.list_selectedcourse.append(self)
    def GetStudentName(self):
        return self.s_name
    def GetStudentRollNumber(self):
        return self.s_id
    def GetStudentID(self):
        return self.m_id
    def dump_student(self):
        return self.s_name
    def AddCart(self):
        self.__cartlist[len(self.__cartlist)] = Cart()

    def GetCart(self, cartindex=0):
        return self.__cartlist[cartindex]

    def BuyCourse(self, course, c_id, cartindex=0):

            try:
                self.__cartlist[cartindex][course.GetCourseName()][1] += course.GetCourseName()
            except:
                self.__cartlist[cartindex].update({c_id: [course.GetCourseName(), course.GetCoursePrice()]})

    def Remove(self, course, c_id, cartindex=0):
        Student.GetCart(self).ShowCart().pop(c_id)

student1 = Student('MT18184','Piyush Srivastava','18184')
student2 = Student('MT18179','Vivek Prakash    ','18179')
student3 = Student('MT18203','Jitendra Yadav   ','18203')
student4 = Student('MT18234','Dimple Dahima    ','18234')
student5 = Student('MT18183','Venugopal        ','18183')
student6 = Student('MT18185','Poornika         ','18185')