class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        stack = []
        for i in range(len(prices)-1, -1  ,-1):
            price = prices[i]

            while stack and stack[-1] > price:
                stack.pop()

            if stack:
                prices[i] = price - stack[-1]
            
            stack.append(price)

        return prices

#################################################
        # stack = []

        # for i in range(len(prices)-1 , -1 , -1):
        #     price = prices[i]

        #     while stack and stack[-1] > price:
        #         stack.pop()
            
        #     if stack:
        #         prices[i] = price - stack[-1]
            
        #     stack.append(price)

        # return prices



#################################################
        # result = []
        # for i in range(len(prices)):
        #     for j in range(i+1 , len(prices)):
        #         if prices[j] <= prices[i]:
        #             result.append(prices[i]-prices[j])
        #             break
        #     else:
        #         result.append(prices[i])
        # return result
        


        