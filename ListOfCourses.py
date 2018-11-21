
class CourseList:

    list_of_courses = []

    def __init__(self):
        self.course_data = []
    def get_courses(self):
        return self.course_data
    @classmethod
    def set_courses(cls,course):
        cls.list_of_courses.append(course)
       # print(cls.list_of_courses[0].c_name)
    def remove_courses(self, c_id):
        try:
            pass
           # defines the way to delete a particular course from the list
        except Exception as e:
            print(e)


    def addcour(self,self1):
        self.list_of_courses.append(self1)
#print(CourseList.list_of_courses)