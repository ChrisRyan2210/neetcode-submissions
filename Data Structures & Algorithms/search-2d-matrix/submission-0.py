class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Data Struc: Array
        # Algo: Binary Search
        # Time:
        # Space

        # Idea: check if number is greater than arr[end], if so then move to next iteration of parent loop 

        for i in range(len(matrix)):
            if target > matrix[i][len(matrix[i]) - 1]:
                continue
            else:
                left = 0
                right = len(matrix[i]) - 1

                while left <= right:
                    mid = (left + right) // 2
                    if target < matrix[i][mid]:
                        right = mid - 1
                    elif target > matrix[i][mid]:
                        left = mid + 1
                    else:
                        return True

                return False
        return False

            