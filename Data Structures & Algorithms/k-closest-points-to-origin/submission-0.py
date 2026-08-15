class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Data Structure: 
        # Time Complexity: O(nlogn)
        # Space Complexity: O(nlogn)
        # Algo: Quick Sort 
            # make last index the pivot
            # calculate the distance from pivot to origin
            # loop through the array and calculate distance at each step
            # if distance < pivot distance then it goes to left otherwise right
            # move the pivot to the middle
            # left/right recursive call, excl the pivot as it is already at correct mid spot
            # once finished sorting: loop through and return k values

        # Example: points = [[0,2],[2,2]], k = 1

        def quickSort(arr, s, e):
            
            # base case (same as mergeSort)
            if e - s + 1 <= 1:
                return arr
            
            pivot = arr[e]
            pivot_dist = pivot[0]**2 + pivot[1]**2 # set pivot point to last index
            left = s # pointer for insert/swap values

            # loop and swap elements smaller than pivot
            for i in range(s, e):
                distance = arr[i][0]**2 + arr[i][1]**2
                if distance < pivot_dist:
                    tmp = arr[left]
                    arr[left] = arr[i]
                    arr[i] = tmp
                    left+=1
            
            # move pivot to middle
            arr[e] = arr[left] # move current middle to end (pivot)
            arr[left] = pivot # move pivot to middle

            # recursive call - excl pivot
            quickSort(arr, s, left - 1) # left 
            quickSort(arr, left + 1, e) # right

            return arr

        sorted_array = quickSort(points, 0, len(points) - 1)

        result = []
        for j in range(k):
            result.append(sorted_array[j])

        return result
