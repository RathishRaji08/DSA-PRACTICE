# Pattern: Two Pointers
# Time: O(n), Space: O(1)
class Solution:
    def maxWater(self, arr):
        n = len(arr)
        l = 0
        r = n - 1
        leftmax = 0
        rightmax = 0
        res = 0
        while l < r:
            if arr[l] <= arr[r]:
                if arr[l] >= leftmax:
                    leftmax = arr[l]
                else:
                    res += leftmax - arr[l]
                l += 1
            else:
                if arr[r] >= rightmax:
                    rightmax = arr[r]
                else:
                    res += rightmax - arr[r]
                r -= 1
        return res