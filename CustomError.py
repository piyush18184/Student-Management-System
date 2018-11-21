class Error(Exception):
    def __init__(self, e):
        self.e = e
    def __str__(self):
        return rep(self.e)
