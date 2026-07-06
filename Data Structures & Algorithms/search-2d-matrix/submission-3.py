class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, m, r = 0, 0, len(matrix) - 1

        while l <= r:
            m = (l + r) // 2

            if matrix[m][0] == target:
                return True
            elif matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1

        row = r
        l, m, r = 0, 0, len(matrix[row]) - 1

        while l <= r:
            m = (l + r) // 2

            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m - 1
            else:
                l = m + 1

        return False
        