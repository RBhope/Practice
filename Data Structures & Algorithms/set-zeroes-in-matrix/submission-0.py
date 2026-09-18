class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    for x in range(cols):
                        if matrix[i][x] != 0:
                            matrix[i][x] = "ZERO"
                    for y in range(rows):
                        if matrix[y][j] != 0:
                            matrix[y][j] = "ZERO"
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "ZERO":
                    matrix[i][j] = 0
                

        