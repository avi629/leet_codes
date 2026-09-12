class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '[':
                stack.append(']')
            elif char == '{':
                stack.append('}')
            else:
                if not stack:
                    return False

                if char != stack[-1]:
                    return False
                    
                stack.pop()

        return len(stack) == 0






############################################################
        # stack =[]
        # match = {')':'(', '}':'{', ']':'['}

        # for char in s:
        #     if char in '({[':
        #         stack.append(char)
    
        #     elif char in ')}]':
        #         if len(stack) == 0:
        #             return False
        #         if stack.pop() != match[char]:
        #             return False
    
        # if len(stack) ==0:
        #     return True
        # else:
        #     return False
        