class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        visited_rows = set()
        visited_cols = set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    visited_rows.add(i)
                    visited_cols.add(j)

        for x in range(rows):
            for y in visited_cols:
                matrix[x][y] = 0
        
        for x in range(cols):
            for y in visited_rows:
                matrix[y][x] = 0


        