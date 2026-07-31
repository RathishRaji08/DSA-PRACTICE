# Pattern: Merge Intervals
# Time: O(n log n), Space: O(n)
class Solution:
    def merge(self, intervals):
        intervals.sort()
        ans = [intervals[0]]
        for start, end in intervals[1:]:
            last_end = ans[-1][1]
            if start <= last_end:
                ans[-1][1] = max(last_end, end)
            else:
                ans.append([start, end])
        return ans