class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        d={}
        for n in nums:
            d[n] = 1 + d.get(n, 0)
        for n, c in d.items():
            buckets[c].append(n)
        ans = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans