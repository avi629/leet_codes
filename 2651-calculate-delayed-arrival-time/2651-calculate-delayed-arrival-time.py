class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        """
        :type arrivalTime: int
        :type delayedTime: int
        :rtype: int
        """
        # return (arrivalTime + delayedTime) % 24

#########################################
        total = arrivalTime + delayedTime
        if total >= 24:
            return total - 24
        return total

        