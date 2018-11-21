class SimilarCourses:
    def __init__(self, c_id, c_name, m_id):
        self.c_id = c_id
        self.c_name = c_name
        self.m_id = m_id
    def dump_course(self):
        return {"course": {"id": self.c_id,
                           "cname": self.c_name,
                           "major_id": self.m_id}}
