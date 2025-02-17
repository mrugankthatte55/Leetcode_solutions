class Solution:
    def numTilePossibilities(self, s: str) -> int:
        freq = Counter(s)
        unique_counts = list(freq.values())
        
        total_count = 0
        
        def count_permutations(selection):
            n = sum(selection)
            denominator = 1
            for x in selection:
                denominator *= factorial(x)
            return factorial(n) // denominator
        
        def sum_over_subsets(index, selection):
            nonlocal total_count
            if index == len(unique_counts):
                if selection:
                    total_count += count_permutations(selection)
                return
            
            for i in range(unique_counts[index] + 1):
                sum_over_subsets(index + 1, selection + ([i] if i > 0 else []))
        
        sum_over_subsets(0, [])
        
        return total_count
        