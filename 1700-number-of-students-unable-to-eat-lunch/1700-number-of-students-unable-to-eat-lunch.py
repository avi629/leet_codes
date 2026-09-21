class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count = 0
        
        while students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count = 0
        
            else:
                student = students.pop(0)
                students.append(student)
                count += 1
        
            if count == len(students):
                break
        
        return len(students)
