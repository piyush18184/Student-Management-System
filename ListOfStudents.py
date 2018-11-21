class TotalStudents:
    def __init__(self):
        self.student_data = []
    def get_students(self):
        return self.student_data
    def set_students(self, student):
        self.student_data.append(student)
    def remove_students(self, s_id):
        try:
            pass
        # Handles the student records
        except Exception as e:
            print(e)