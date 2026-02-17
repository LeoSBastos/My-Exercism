from xeger import Xeger

class Robot:
    def __init__(self):
        self.name = Xeger().xeger(r'^[A-Z]{2}\d{3}$')
    
    def reset(self):
        self.__init__()