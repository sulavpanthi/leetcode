class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalSum = numBottles
        while numBottles >= numExchange:
            exchangedBottles = numBottles // numExchange
            totalSum += exchangedBottles
            numBottles = exchangedBottles + numBottles % numExchange
        return totalSum