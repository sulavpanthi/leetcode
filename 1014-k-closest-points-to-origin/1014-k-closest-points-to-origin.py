from heapq import heappush, heappop
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        result = []
        for point in points:
            distance = math.sqrt((point[0])**2 + (point[1])**2)
            
            # check if heap is full
            if len(result) == k and -result[0][0] > distance:
                heappop(result)
            elif len(result) == k and -result[0][0] <= distance:
                continue
            heappush(result, (-distance, point[0], point[1]))

        return [each[1:] for each in result]