class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        depth = 0
        for i in range(len(s)):
            if s[i] == "(":
                depth += 1
                if depth > 1:
                    result = result + s[i]
            else:
                depth -= 1
                if depth > 0:
                    result = result + s[i]
            
        return result
