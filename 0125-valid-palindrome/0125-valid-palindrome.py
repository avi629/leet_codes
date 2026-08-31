class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()              # ignore capitalization
        left = 0
        right = len(s) -1

        while left < right:

            while left < right and not s[left].isalnum(): # skip spc/pucn
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True
        

##################################################################
        # s = s.lower()           # convert to lower case
        # clean_string = ""

        # for char in s:
        #     if char.isalnum():  # keep only letters and numbers
        #         clean_string += char

        # length = len(clean_string)
        # mid = length // 2

        # first_half = clean_string[0:mid]
        # if length % 2 == 0:                          #it handle if the mid is odd
        #     second_half = clean_string[mid:length]
        # else:
        #     second_half = clean_string[mid+1:length]

        # reverse_second = ""
        # for i in range(len(second_half) - 1, -1, -1):
        #     reverse_second += second_half[i]

        # return first_half == reverse_second
        

