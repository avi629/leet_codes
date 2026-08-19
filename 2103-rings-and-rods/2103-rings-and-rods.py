class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        rods = [set() for _ in range(10)]

        for i in range(0,len(rings) , 2):
            colour = rings[i]
            rod = int(rings[i+1])

            rods[rod].add(colour)

            count = 0
            for rod in rods:
                if len(rod) == 3:
                    count += 1
            
        return count