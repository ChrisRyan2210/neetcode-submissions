class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        # keep a normal counter where grump[i] = 0 to track happy customers
        # for any window -> we want to find the values that we are misssing out on because he is grump
        # so for each window -> keep track of sum for that window where grump[i] = 1 and track = max(track, sum)
        # then we can just return the addition of the 2 results

        # customers = [1,0,1,2,1,1,7,5]
        # grumpy =    [0,1,0,1,0,1,0,1]
        # our grump[i] = 0 counter would be 10 
        # our max window tracker where grump[i] = 1 would be 6
        # return 10 + 6, correct

        l = 0 
        m = 0
        notGrumpyCount = 0
        grumpyCount = 0

        for r in range(len(customers)):
            # get our non-grump value
            if grumpy[r] == 0:
                notGrumpyCount += customers[r]
            # sliding window to find out the max customers we miss in the given window "minutes"
            if grumpy[r] == 1: 
                grumpyCount += customers[r]
            print(grumpyCount)
            if (r - l + 1) > minutes:
                if grumpy[l] == 1:
                    grumpyCount -= customers[l]
                l += 1
            if (r - l + 1) == minutes:
                m = max(m, grumpyCount)
        return m + notGrumpyCount