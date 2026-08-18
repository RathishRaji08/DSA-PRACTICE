# Pattern: Binary Search (treat 2D matrix as flattened 1D array)
# Time: O(log(m*n)), Space: O(1)
class Solution(object):
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        l = 0
        h = (n * m) - 1
        while l <= h:
            mid = (l + h) // 2
            row = mid // m
            col = mid % m
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                h = mid - 1
        return False