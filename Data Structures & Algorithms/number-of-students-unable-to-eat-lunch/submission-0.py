class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # 0 = circular
        # 1 = square
        # len(students) = len(sandwiches)
        # sandwiches is a stack (LIFO): sandwiches[0] = top of stack
        # students is a queue (FIFO): students[0] = left/front of queue
        # for loop wont work as we need it to keep looping indefinitely until x
        # while loop should work 
        counter = 0
        while students:
            # break out if counter >= len(students)
            if counter >= len(students):
                break
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                counter = 0
            else:
                student = students.pop(0)
                students.append(student)
                counter +=1
        return len(students)
