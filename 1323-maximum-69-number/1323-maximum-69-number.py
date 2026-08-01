class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = list(str(num))
        for i in range(len(digits)):
            if digits[i] == '6':
                digits[i] = '9'
                break
        result = int(''.join(digits))
        return result

######################################################
        original = num
        place = 1
        six_place = 0
        while num != 0:
            digit = num % 10   #6
            if digit == 6:
                six_place = place
            place = place * 10
            num = num // 10
        final_answer = original + (3 * six_place)
        return final_answer