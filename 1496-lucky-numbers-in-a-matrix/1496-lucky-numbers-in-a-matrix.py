class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows = len(matrix)
        for idx, row in enumerate(matrix):

            # find min element and index of that min element
            min_element, min_index = (float("inf"), float("inf"))
            for index, element in enumerate(row):
                if element < min_element:
                    min_element = element
                    min_index = index

            # find max element in the same col index
            max_element = float("-inf")
            row_range = set(range(rows)) - {idx}
            for each_row in row_range:
                max_element = max(max_element, matrix[each_row][min_index])
            if min_element >= max_element:
                result.append(min_element)

        return result