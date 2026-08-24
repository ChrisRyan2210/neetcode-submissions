class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                s = stack.pop()
                result[s] = i - s
            stack.append(i)

        return result







        # #brute force answer

        # for i in range(len(temperatures)):
        #     j = i + 1
        #     while j < len(temperatures):
        #         if temperatures[i] >= temperatures[j]:
        #             j += 1
        #         else:
        #             result[i] = j - i
        #             break
        
        # result[-1] = 0
        # return result
            
            
