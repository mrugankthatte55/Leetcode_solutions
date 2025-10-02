class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        a = 1
        b = 2 * numExchange - 3
        c = -2 * numBottles
        d = b * b - 4 * a * c
        t = math.ceil((-b + math.sqrt(d)) / (2 * a))
        return numBottles + t - 1