class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        window = set()
        l = 0

        for r in range(len(nums)):
            # we want to remove the left most item of window if index r - l is greater than k
            
            # check if already in window, if so return True, else add it to window
            if nums[r] in window:
                return True
            window.add(nums[r])
            if r - l  >= k:
                window.remove(nums[l])
                l += 1
        return False