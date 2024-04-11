class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        a = []
        for digit in num:
            while k and a and a[-1] > digit:
                a.pop()
                k -= 1
        
            a.append(digit)
        ans = a[:-k] if k else a
        return "".join(ans).lstrip('0') or "0"