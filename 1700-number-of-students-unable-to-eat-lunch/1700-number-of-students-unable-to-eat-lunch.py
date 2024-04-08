class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n=len(students)
        for _ in range(n*n):
            if len(students)==0:
                return 0
            elif students[0]==sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                a=students.pop(0)
                students.append(a)
        return(len(students))