class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0 :
            return False

        while n % 2 == 0:
            n = n //2
        while n % 3 == 0:
            n = n // 3
        while n % 5 == 0:
            n = n // 5

        return n == 1










# n
# │
# ├── Divide by 2 as much as possible
# │
# ├── Divide by 3 as much as possible
# │
# ├── Divide by 5 as much as possible
# │
# └── Is the remaining number 1?
#       │
#       ├── Yes → Ugly Number ✅
#       └── No  → Not Ugly Number ❌
            