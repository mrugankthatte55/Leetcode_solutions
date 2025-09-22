class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n = len(nums)

        events = {}
        for x in nums:
            events[x - k] = events.get(x - k, 0) + 1
            events[x + k + 1] = events.get(x + k + 1, 0) - 1

        max_r = 0
        cur = 0
        prev = None
        for point in sorted(events):
            if prev is not None and point > prev:
                if cur > max_r:
                    max_r = cur
            cur += events[point]
            prev = point
        best_any_T = min(numOperations, max_r)

        best_existing_v = 0

        i = 0
        while i < n:
            j = i + 1
            while j < n and nums[j] == nums[i]:
                j += 1
            v = nums[i]
            f = j - i
            L = bisect_left(nums, v - k)
            R = bisect_right(nums, v + k)
            r = R - L
            best_existing_v = max(best_existing_v, min(r, f + numOperations))
            i = j

        return max(best_any_T, best_existing_v)
