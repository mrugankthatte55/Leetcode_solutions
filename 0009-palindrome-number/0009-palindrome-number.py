class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        a = []
        for i in str(x):
            a.append(int(i))
        if(a==a[::-1]):
            return True
        return False