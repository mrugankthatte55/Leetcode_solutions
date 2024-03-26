class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        a = [int(d) for d in str(x)]
        if(a==a[::-1]):
            return True
        return False