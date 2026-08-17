class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Data Struc: Array
        # Algo: Binary Search
        # Time: O(log(m+n))
        # Space: O(1)

        # Do binary search on rows

        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bot = rows - 1

        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not top <= bot:
            return False

        row = (top + bot) // 2
        left, right = 0, cols - 1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1 
            else:
                return True
        return False

        # # Old method O(mlogn)
        # # Idea: check if number is greater than arr[end], if so then move to next iteration of parent loop 

        # for i in range(len(matrix)):
        #     if target > matrix[i][len(matrix[i]) - 1]:
        #         continue
        #     else:
        #         left = 0
        #         right = len(matrix[i]) - 1

        #         while left <= right:
        #             mid = (left + right) // 2
        #             if target < matrix[i][mid]:
        #                 right = mid - 1
        #             elif target > matrix[i][mid]:
        #                 left = mid + 1
        #             else:
        #                 return True

        #         return False
        # return False

            