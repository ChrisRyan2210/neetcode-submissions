class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        self.prefix = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            self.prefix.append(total)

        rightSum = self.prefix[-1]
        print(rightSum)

        for i in range(len(nums)):
            leftSum = self.prefix[i-1] if i > 0 else 0
            print(leftSum)
            if rightSum - nums[i] == leftSum*2:
                return i
        return -1

        
        
          



        
        
        
