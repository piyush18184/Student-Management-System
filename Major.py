class Major:
    def __init__(self, m_id, m_name):
        self.m_id = m_id
        self.m_name = m_name
    def dump_major(self):
        return {"major": {"m_id": self.m_id,
                            "m_name": self.m_name}}
