class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Data Struc: Array
        # Algo: Bucket Sort
        # Time: O(n)
        # Space: O(m-n) which is assumed to be a constant so O(1)

        # implement array of 0s for counting
        counts = [0, 0, 0]

        # increment the counter array
        for n in nums:
            counts[n] +=1

        k = 0 # index for inserting values
        
        for i in range(len(counts)):
            for j in range(counts[i]):
                nums[k] = i 
                k+=1
        return nums
