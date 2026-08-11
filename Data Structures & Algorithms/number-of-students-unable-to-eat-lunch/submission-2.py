class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # the trick is that the order of students doesnt matter but the order of sandwiches does. 
        # if the number of 1/0 dont match: there will be someone left over
        # we do a counter on Students and then loop through sandwhiches, decrementing the counter until we find a val = 0

        s_map = {}
        for i in students:
            if i in s_map:
                s_map[i] +=1
            else:
                s_map[i] = 1
        print(s_map)
        
        counter = len(students)
        for j in sandwiches:
            if j not in s_map:
                return counter
            if s_map[j] == 0:
                break
            else:
                s_map[j] -=1
                counter -=1
        return counter
        
        
