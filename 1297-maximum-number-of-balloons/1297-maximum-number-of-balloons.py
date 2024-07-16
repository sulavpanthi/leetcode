class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import defaultdict, Counter
        temp = defaultdict(int)
        result = 0
        for each in text:
            if each in ['b', 'a', 'l', 'o', 'n']:
                temp[each] += 1
        if not len(temp.keys()) == 5: return result
        balloon_counter = Counter("balloon")
        for each in balloon_counter.keys():
            temp[each] //= balloon_counter[each]
        result = min(temp.values())
        return result