import statistics

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        max_jump = max(stones)
        n = len(stones)

        # edge cases
        if n > 1 and stones[1] - stones[0] != 1: return False
        median = statistics.median(stones)
        mean = statistics.mean(stones)
        if mean > 2*median: return False


        # # Approach 1: Using memoization
        # dp = [[-1] * (max_jump+1) for _ in range(n)]
        # def recur_fn(prev_index, index, jumps):
        #     """
        #     index: current index
        #     jumps: jump taken to reach this unit
        #     """
        #     print(f"\n\nindex {index} with val {stones[index]} and jumps {jumps}")
            
        #     # handle out of bound cases
        #     if index >= n: return False
        #     if jumps < 1 or jumps > max_jump:
        #         return False

        #     print("dp array", dp[index][jumps])

        #     # check dp array
        #     if dp[index][jumps] != -1:
        #         return dp[index][jumps]

        #     # handle base cases of recursion
        #     if index == n-1:
        #         if (stones[n-1] - stones[prev_index]) == jumps:
        #             return True
        #         else:
        #             return False
        #     if not (stones[index] - stones[prev_index]) == jumps:
        #         return False
        #     print("matched the jumps with units", index, stones[index], jumps)
        #     possible_jumps = [jumps - 1, jumps, jumps + 1]
        #     res = False

        #     for jump in possible_jumps:
        #         if jump < 1: continue
        #         future = index + 1
        #         print(f"inner loop future {future} with jump {jump} and dp array {dp[index][jumps]}")
        #         while True:
        #             if future >= n: break
        #             if stones[future] == stones[index] + jump:
        #                 print(f"\n\n(i) {index} -> {future} [{jump}]")
        #                 res = recur_fn(index, future, jump) or res
        #                 break
        #             elif stones[future] > stones[index] + jump:
        #                 break
        #             else:
        #                 future += 1

        #     dp[index][jumps] = res
        #     return res
        # result = recur_fn(0, 1, 1)
        
        
        
        
        # Approach 2: Using tabulation
        stack = [(1, 1)]
        visited = set((0,1))
        while len(stack) > 0:
            index, jump = stack.pop()
            print(f"Processing index {index} with jump {jump}")
            if index == n - 1: return True

            for next_jump in [jump - 1, jump, jump + 1]:
                if next_jump < 1: continue
                future = index + 1
                while future < len(stones) and stones[future] <= (stones[index] + next_jump):
                    if stones[future] == stones[index] + next_jump:
                        if (future, next_jump) not in visited:
                            stack.append((future, next_jump))
                            visited.add((future, next_jump))
                            break
                    future += 1

        return False


        return result