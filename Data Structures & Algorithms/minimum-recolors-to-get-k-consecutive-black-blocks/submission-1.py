class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        # k means that we have a fixed window
        # we want to slide this window along the array and check if the window is valid
        # the catch is we can change w to b 
        # so at each iteration we run a counter that counts the number of W 
        # update result to be the min of (res, counter)

        # BBWBWWB, k = 3
        # 1st iteration: WBWBBBW


        r = l = 0 
        res = k
        counter = 0 


        for r in range(len(blocks)):
            if blocks[r] == 'W':
                counter += 1
            if (r - l + 1) > k:
                if blocks[l] == 'W':
                    counter -= 1
                l += 1
            if (r - l + 1) == k:
                res = min(res, counter) 
        return res
            