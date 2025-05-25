class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = Counter(words)
        length = 0
        used_middle = False

        for word in list(d.keys()):
            rev = word[::-1]
            if word == rev:
                pairs = d[word] // 2
                length += pairs * 4
                d[word] -= pairs * 2
            else:
                if rev in d:
                    pairs = min(d[word], d[rev])
                    length += pairs * 4
                    d[word] -= pairs
                    d[rev] -= pairs

        for word in d:
            if word == word[::-1] and d[word] > 0:
                length += 2
                break

        return length
