class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        parts = date.split('-') 
        year = int(parts[0]) 
        month = int(parts[1])  # op- "02" to 2
        day = int(parts[2])

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month[1] = 29  # for leap year
        total = 0
        for i in range(0 , month - 1):
            total = total + days_in_month[i]
        
        return total + day
            


