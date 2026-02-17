class Matrix:
    def __init__(self, matrix_string):
        rowsString = matrix_string.split("\n")
        self.rows = [[] for x in rowsString]
        for i in range(len(rowsString)):
            self.rows[i] = [int(x) for x in rowsString[i].split(" ")]
        self.columns =[[] for x in range(len(self.rows[0]))]
        for r in self.rows:
            for i in range(len(r)):
                self.columns[i].append(r[i])
    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.columns[index-1]