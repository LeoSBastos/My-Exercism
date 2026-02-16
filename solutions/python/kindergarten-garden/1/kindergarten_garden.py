"""
Kindergarten Garden
"""
defaultStudents = ['Alice', 'Bob', 'Charlie', 'David','Eve', 'Fred', 'Ginny', 'Harriet','Ileana', 'Joseph', 'Kincaid', 'Larry']

class Garden:
    def __init__(self, diagram, students=defaultStudents):
        """
        Initializer
        """
        self.students = sorted(students)
        (self.row1, self.row2) = diagram.split('\n')
        self.plantsDict = {'G': 'Grass','C': 'Clover','R':'Radishes','V':'Violets'}    
    def plants(self, student):
        """
        Plants by student
        """
        pos = self.students.index(student)
        return [self.plantsDict[self.row1[2*pos]],self.plantsDict[self.row1[(2*pos)+1]],self.plantsDict[self.row2[2*pos]],self.plantsDict[self.row2[(2*pos)+1]]]

