# Pattern: Kadane's Algorithm (Dynamic Programming)
# Time: O(n), Space: O(1)
class Solution:
    def maxSubarraySum(self, arr):
        cur_sum = arr[0]
        max_sum = arr[0]
        for i in range(1, len(arr)):
            cur_sum = max(arr[i], (cur_sum + arr[i]))
            max_sum = max(max_sum, cur_sum)
        return max_sum