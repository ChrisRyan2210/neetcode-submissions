class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1
            
        while j >= 0:
            nums1[k] = nums2[j]
            j-=1
            k-=1
        





        # ## USING MERGE SORT METHOD -- NOT OPTIMAL
        # # use merge sort algo without the recursion
        # # this very similar to merging two sorted linked lists
        
        # # store base arrays to grab values from below
        # L = nums1[:m].copy()
        # R = nums2.copy()
        
        # # three ptrs 
        # i = 0 # for nums1
        # j = 0 # for nums2
        # k = 0 # in merge_sort recrusive it would be k = s but here just nums1[0] ->

        # # nums1 is always bigger but still need to check if nums2 is not empty
        # while i < len(L) and j < len(R):
        #     if L[i] <= R[j]:
        #         nums1[k] = L[i]
        #         i+=1
        #     else:
        #         nums1[k] = R[j]
        #         j+=1
        #     k+=1
        #     print(nums1[k])
        
        # while i < len(L):
        #     nums1[k] = L[i]
        #     i+=1
        #     k+=1
        
        # while j < len(R):
        #     nums1[k] = R[j]
        #     j+=1
        #     k+=1
