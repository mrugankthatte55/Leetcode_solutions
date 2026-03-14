class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def generate_sequences(chars, n, last_char=None, current_str=""):
            if n == 0:
                yield current_str
                return
            for char in chars:
                if char != last_char:
                    yield from generate_sequences(chars, n - 1, char, current_str + char)

        # Usage
        chars = ['a', 'b', 'c']
        results = list(generate_sequences(chars, n))

        results.sort()
        if len(results)>=k:
            return results[k-1]
        return ""

