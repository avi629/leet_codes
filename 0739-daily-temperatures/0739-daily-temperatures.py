class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                answer[index] = i - index
            
            stack.append(i)

        return answer


###########################################################
        # answer = [0] * len(temperatures)
        # stack = []

        # for i in range(len(temperatures)):
        #     while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
        #         index = stack.pop()
        #         answer[index] = i - index
                
        #     stack.append(i)
        # return answer


        # answer = [0] * len(temperatures)
        # for i in range(len(temperatures)):
        #     for j in range(i + 1 , len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             answer[i] = j - i
        #             break
        # return answer

        