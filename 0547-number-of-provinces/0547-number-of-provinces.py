class DisjointSet:
    def __init__(self, num):
        self.parent = [i for i in range(num)]
        self.rank = [0 for _ in range(num)]

    def find(self, key):
        if self.parent[key] != key:
            self.parent[key] = self.find(self.parent[key])
        return self.parent[key]

    def union(self, x, y):
        X = self.find(x)
        Y = self.find(y)
        if X != Y:
            rank1 = self.rank[X]
            rank2 = self.rank[Y]
            if rank1 < rank2:
                self.parent[X] = Y
            elif rank2 < rank1:
                self.parent[Y] = X
            else:
                self.parent[Y] = X
                self.rank[X] += 1


class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num_rows = len(isConnected)
        num_cols = len(isConnected[0])

        ds = DisjointSet(num_rows)
        for i in range(num_rows):
            for j in range(i+1, num_cols):
                if isConnected[i][j] == 1:
                    ds.union(i, j)
        unique_parents = set(ds.find(i) for i in range(num_rows))
        return len(unique_parents)