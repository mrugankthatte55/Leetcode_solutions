import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = [i for i in s.lower() if i.isalnum()]
        return a == a[::-1]
        