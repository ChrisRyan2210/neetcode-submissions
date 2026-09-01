class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        # loop through, check if r - l <= k -> if it is then check if average is greater than threshold -> otherwise move left ptr forward

        # keep track of sum up to current point, if we need to remove the left value, just subtract that value from sum and then calculate our avg by dividing by r - l

        # [2,2,2,2,5,5,5,8], k = 3, thresholh = 4
        # is r - l >= k: no
            # [2], sum += arr[r]
            # avg = sum / r - l
        # ... we get to r = 3 , so "2"
        # is r - l >= k: yes
            # sum -= arr[l]
            # sum += arr[r]


        res = 0
        l = 0
        total = 0
        # ctr = set()
        
        for r in range(len(arr)):
            if r - l >= k:
                total -= arr[l]
                # total += arr[r]
                l += 1
            total += arr[r]
            avg = total / (r - l + 1)
            if avg >= threshold and r - l + 1 == k:
                # print(f"r:{r}, l{l}")
                res += 1
        
        return res