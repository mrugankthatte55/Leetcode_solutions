class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        freqPrev, freqNext = Counter(), Counter(nums)
        count = 0
        for i in nums:
            freqNext[i] -= 1
            count += freqPrev[i*2] * freqNext[i*2]
            freqPrev[i] += 1
        return count % (10**9 + 7)