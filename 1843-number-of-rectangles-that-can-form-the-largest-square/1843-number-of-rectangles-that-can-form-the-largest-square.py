class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        count = 0
        max_length = 0
        for each in rectangles:
            min_length = min(each[0], each[1])
            max_length = max(min_length, max_length)
        for each in rectangles:
            if max_length <= each[0] and max_length <= each[1]:
                count += 1
        return count