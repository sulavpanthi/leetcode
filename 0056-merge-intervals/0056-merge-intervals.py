class Solution:

    def overlap(self, first, second):
        if second[0] <= first[1]:
            return True
        return False

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for each in intervals[1:]:
            last = res[-1]
            if self.overlap(last, each):
                last[0] = min(last[0], each[0])
                last[1] = max(last[1], each[1])
            else:
                res.append(each)

        return res