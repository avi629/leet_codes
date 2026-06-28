class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(prices)):
            for j in range(i+1 , len(prices)):
                if prices[j] <= prices[i]:
                    result.append(prices[i]-prices[j])
                    break
            else:
                result.append(prices[i])
        return result
        


        