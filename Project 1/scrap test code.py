matrix = [[1,2,3],[4,'_',6],[7,8,9]]
def findBlank(matrix):
    for x in range(len(matrix)):
        for h in range(len(matrix[x])):
            if matrix[x][h] == "_":
                return str(x)+str(h)
result = findBlank(matrix)
print(result)
