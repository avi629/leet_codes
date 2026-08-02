class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """
        used = 0
        dist = 0
        while mainTank > 0:
            mainTank = mainTank - 1
            dist = dist + 10
            used = used + 1

            if used == 5:
                if additionalTank > 0:
                    mainTank = mainTank + 1
                    additionalTank = additionalTank - 1
                used = 0
                
        return dist
                    

