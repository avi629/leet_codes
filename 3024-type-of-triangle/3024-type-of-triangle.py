class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        a , b , c = sorted(nums)

        if a + b <= c:
            return "none"
        
        if a == b == c:
            return "equilateral"
        elif a == b != c or b == c != a or a == c != b:
            return "isosceles"
        else:
            return "scalene"
