class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        result = [0] * n
        skip = False
        index_in_deck = 0
        index_in_result = 0
        deck.sort()
        while index_in_deck < n:
            if result[index_in_result] == 0:
                if not skip:
                    result[index_in_result] = deck[index_in_deck]
                    index_in_deck += 1
                skip = not skip
            index_in_result = (index_in_result + 1) % n
        return result