class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_dict = {}
        for i, num in enumerate(nums):
            search_for = target - num
            # print("search 1", search_for)
            if search_for in temp_dict:
                return [temp_dict[search_for], i]
            else:
                temp_dict[num] = i
            # print("search", search_for, temp_dict)
        return []