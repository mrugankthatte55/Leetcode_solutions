class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ans = 0
        n = len(baskets)
        for i in fruits:
            t = 1
            for j in range(n):
                if i <= baskets[j]:
                    baskets[j] = 0
                    t = 0
                    break
            ans += t
        return ans