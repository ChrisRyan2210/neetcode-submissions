class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Data Struc: Array
        # Algo: Binary Search
        # Time: O(log(m+n))
        # Space: O(1)

        # Get number of rows and cols
        rows = len(matrix) 
        cols = len(matrix[0])

        # Pinters to top and bottom rows
        top = 0
        bot = rows - 1

        while top <= bot:
            row = (top + bot) // 2 # Gets the middle row
            if target > matrix[row][-1]:
                top = row + 1 # shift down a row
            elif target < matrix[row][0]:
                bot = row - 1 # shift up a row
            else:
                break # target is between curr row s and e
        
        # if loop ended becasue top > bot then target does not exist inside any sub array
        if not top <= bot:
            return False

        row = (top + bot) // 2 # set the current row
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

            