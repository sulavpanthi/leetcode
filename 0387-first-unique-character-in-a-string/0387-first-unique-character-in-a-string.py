class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}
        array = []
        for index, value in enumerate(s):
            if value not in hash_map:
                array.append(index)
                hash_map[value] = index
            else:
                if hash_map[value] is not None:
                    array.remove(hash_map[value])
                hash_map[value] = None
        if len(array) >= 1:
            return array[0]
        return -1