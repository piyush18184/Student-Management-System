class MajorList:
    def __init__(self):
        self.major_data = []
    def get_major_data(self):
        return self.major_data
    def set_major_data(self, major):
        self.major_data.append(major)
    def remove_major_data(self, m_id):
        try:
            pass
        # Stores a way to remove the major from the list
        except Exception as e:
            print(e)