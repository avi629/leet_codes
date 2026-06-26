class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""                   #Check if a GCD exists

        from math import gcd           # Step 2: Find the GCD length
        length = gcd(len(str1),len(str2))

        return str1[0:length]   # return slice the first length characters from str1
        