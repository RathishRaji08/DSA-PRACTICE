# Pattern: Merge Sort (Divide and Conquer)
# Time: O(n log n), Space: O(n)
class Solution:
    def inversionCount(self, arr):
        def merge_sort(low, high):
            if low >= high:
                return 0
            mid = (low + high) // 2
            inv = merge_sort(low, mid)
            inv += merge_sort(mid + 1, high)
            inv += merge(low, mid, high)
            return inv

        def merge(low, mid, high):
            temp = []
            left = low
            right = mid + 1
            inv = 0
            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    inv += (mid - left + 1)
                    right += 1
            while left <= mid:
                temp.append(arr[left])
                left += 1
            while right <= high:
                temp.append(arr[right])
                right += 1
            for i in range(low, high + 1):
                arr[i] = temp[i - low]
            return inv

        return merge_sort(0, len(arr) - 1)