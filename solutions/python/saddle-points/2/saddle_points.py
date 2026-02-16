def saddle_points(matrix):
    result = []
    if matrix:
        columnLen = len(matrix[0]) 
        for row in matrix:
            if len(row) != columnLen:
                raise ValueError("irregular matrix")
        for i,row in enumerate(matrix):
            for j,col in enumerate(row):
                if col == max(row) and col == min([row[j] for row in matrix]):
                    result.append({"row": i+1, "column": j+1})
    return result