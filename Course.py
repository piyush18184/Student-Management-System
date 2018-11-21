from ListOfCourses import CourseList
class Courses:
    count = 0
    list_course= [];
    def __init__(self, c_id, c_name,c_price):
        self.c_id = c_id
        self.c_name = c_name
        self.c_price=c_price
        Courses.count = Courses.count + 1
        CourseList.set_courses(self)
        self.list_course.append(self)
    def dump_course(self):
        return self.c_id
        return self.c_name
        return self.c_price

    def GetCourseName(self):
        return self.c_name
    def GetCourseID(self):
        return self.c_id
    def GetCoursePrice(self):
        return self.c_price

course1 = Courses('ECE501','PDCS',2000)
course2 = Courses('ECE543','WC  ',1000)
course3 = Courses('ECE523','IA  ',2500)
course4 = Courses('MT111 ','PRP ',1500)
course5 = Courses('CSE511','ML  ',1800)
course6 = Courses('CSE532','AI  ',3000)
course7 = Courses('PHI555','POR ',500)
course8 = Courses('ECE333','DPS ',5000)
course9 = Courses('ECE113','RR  ',2500)