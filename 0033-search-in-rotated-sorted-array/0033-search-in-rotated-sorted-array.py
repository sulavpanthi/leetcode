class Solution:

    def search(self, nums: List[int], target: int) -> int:
        # nums = [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
        self.nums = nums
        index_range = [0]
        right_index = len(nums) - 1

        return self.init(nums, target, 0, right_index)


    def init(self, array, target, left_index, right_index):
        array_length = len(array)
        mid = array_length // 2
        print("array and mid", array, mid, left_index, right_index)
        if array_length == 0:
            return -1
        if array_length == 1 and target != array[0]:
            return -1
        if target == array[mid]:
            return left_index + mid
        elif target == self.nums[left_index]:
            return left_index
        elif target == self.nums[right_index]:
            return right_index
        else:
            left_array = array[:mid]
            right_array = array[mid + 1:]
            if target < array[mid]:
                if target < left_array[0] and left_array[0] < array[mid]:
                    next_array = right_array
                    left_index += mid + 1
                else:
                    next_array = left_array
                    right_index -= mid
            else:
                if target > left_array[0] and left_array[0] > array[mid]:
                    next_array = left_array
                    right_index -= mid
                else:
                    next_array = right_array
                    left_index += mid + 1
            print("end", next_array, left_index, right_index)
            return self.init(next_array, target, left_index, right_index)


    
