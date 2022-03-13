def islenad(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if((i == 0 or i == len(matrix) -1)):
                if(matrix[i][j] == 1):
                    matrix[i][j] = 0
            if(j == 0 or j == len(matrix) ):
                if(matrix[i][j] == 1):
                    matrix[i][j] = 0
            if(matrix[i][j] == 0):
                matrix[i][j] = " "
    return matrix
           
    
matrix = [[1,1,1,1,1,1,1],
          [1,0,1,0,0,0,1],
          [1,0,0,0,0,0,1],
          [1,0,0,1,0,0,1],
          [1,0,0,0,1,0,1],
          [1,1,1,1,1,1,1]]
matrix = islenad(matrix=matrix)
print(matrix)