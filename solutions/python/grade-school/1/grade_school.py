"""
Grade Scholl
"""

class School:
    def __init__(self):
        """
        Initiating class
        """
        self.students = []
        self.grades = []
        self.dic = dict()
        self.addedList = []

    def add_student(self, name, grade):
        """
        Add student function
        """
        if name not in self.dic:
            self.dic[name] = grade
            self.addedList.append(True)
        else:
            self.addedList.append(False) 

    def roster(self):
        """
        Rooster function
        """
        print(list(self.dic.keys()))
        return [x for (x,y) in sorted(self.dic.items(), key=lambda x: (x[1],x[0]))]

    def grade(self, grade_number):
        """
        Grade function
        """
        aux = []
        for x in iter(self.dic):
            if self.dic[x] == grade_number:
                aux.append(x)
        return sorted(aux)
    
    def added(self):
        """
        Added function
        """
        return self.addedList