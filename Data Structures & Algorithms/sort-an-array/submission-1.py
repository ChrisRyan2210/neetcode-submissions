import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # Data Struc: Array
        # Algo: Quick Sort
        # Time: O(nlogn)
        
        # we want to pick a pivot point and swap it with current index if its less than value
        def quickSort(arr, s, e):

            if e - s + 1 <= 1:
                return arr

            p_idx = random.randint(s, e)
            pivot = arr[p_idx]
            arr[p_idx], arr[e] = arr[e], arr[p_idx]

            k = s
            for i in range(s, e):
                if arr[i] <= pivot:
                    tmp = arr[k]
                    arr[k] = arr[i]
                    arr[i] = tmp
                    k += 1
        
            # swap pivot and k
            arr[e] = arr[k]
            arr[k] = pivot  

            quickSort(arr, s, k-1) 
            quickSort(arr, k+1, e)
            
            return arr

        return quickSort(nums, 0, len(nums) - 1)
        