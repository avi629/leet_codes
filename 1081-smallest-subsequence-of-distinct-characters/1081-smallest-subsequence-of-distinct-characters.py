class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_occu = {}
        for i , c in enumerate(s):
            last_occu[c] = i

        stack = []
        in_stack = set()

        for i, c in enumerate(s):
            if c in stack:
                continue
            while stack and stack[-1] > c and i < last_occu[stack[-1]]:
                removed = stack.pop()
                in_stack.remove(removed)

            stack.append(c)
            in_stack.add(c)

        return ''.join(stack)