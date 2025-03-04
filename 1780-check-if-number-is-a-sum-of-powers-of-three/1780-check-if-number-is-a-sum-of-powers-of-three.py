class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        arr=[1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969]
        def generate_combinations(arr, n):
            def backtrack(start, path, length):
                if len(path) == length:
                    
                    combinations.add(sum(path))
                    return
                for i in range(start, len(arr)):
                    backtrack(i + 1, path + [arr[i]], length)
            
            combinations = set()
            for length in range(1, n + 1):
                backtrack(0, [], length)
            
            return sorted(combinations)
        arr2=generate_combinations(arr,len(arr))
        if n in arr2:
            return True
        return False