class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # for i in range(len(digits)-1 , -1 , -1):
        #     if digits[i] < 9 : #If digit lessthan 9, just add 1 and return
        #         digits[i] +=1
        #         return digits

        #     digits[i] = 0  #If digit is 9, make it 0 and continue carry

        # return [1] + digits #If all digits were 9, we reach here

############################################################
        for i in range(len(digits)-1 , -1 , -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0
        
        return [1] + digits