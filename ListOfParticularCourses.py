class SimilarCoursesList:
    def __init__(self):
        self.particular_course_data = []
    def get_similarcourses(self):
        return self.particular_course_data
    def set_similarcourses(self, course):
        self.particular_course_data.append(course)
    def remove_similarcourses(self, c_id):
        try:
            pass
        # Handles a way to sort similar courses
        except Exception as e:
            print(e)