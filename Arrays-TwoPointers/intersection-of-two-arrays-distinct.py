# Problem: Intersection of Arrays with Distinct Elements
# Platform: GeeksforGeeks
# Link: https://www.geeksforgeeks.org/problems/intersection-of-two-arrays2404/1
# Difficulty: Easy
# Pattern: Two Pointers (after sorting)
# Time: O(n log n + m log m), Space: O(1)

class Solution:
    def intersectSize(self, a, b):
        count = 0
        a.sort()
        b.sort()
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                count += 1
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1
        return count