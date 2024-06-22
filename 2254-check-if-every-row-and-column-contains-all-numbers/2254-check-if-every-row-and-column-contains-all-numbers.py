class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        # brute force approach
        for i in range(len(matrix)):
            row = matrix[i]
            n = len(row)
            new_set = set(range(1, n+1))
            row_set = set(row)
            if row_set != new_set:
                return False

        # for columns
        for j in range(len(matrix[0])):
            n = len(matrix[0])
            new_set = set(range(1, n+1))
            column_list = []
            for i in range(len(matrix[0])):
                column_list.append(matrix[i][j])
            if new_set != set(column_list):
                return False
                
        return True