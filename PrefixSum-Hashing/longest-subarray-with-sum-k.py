# Problem: Longest Subarray with Sum K
# Platform: GeeksforGeeks
# Difficulty: Medium
# Pattern: Prefix Sum + Hashing
# Time: O(n), Space: O(n)

class Solution:
    def longestSubarray(self, arr, k):
        curr_sum = longest = 0
        prefix = {}
        for i in range(len(arr)):
            curr_sum += arr[i]
            if curr_sum == k:
                longest = i + 1
            need = curr_sum - k
            if need in prefix:
                length = i - prefix[need]
                longest = max(longest, length)
            if curr_sum not in prefix:
                prefix[curr_sum] = i
        return longest