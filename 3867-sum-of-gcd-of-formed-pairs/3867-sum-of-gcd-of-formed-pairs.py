class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        mxi = 0
        prefixGcd= []
        n = len(nums)
        for i in range(n):
            mxi = max(mxi, nums[i])
            prefixGcd.append(gcd(nums[i], mxi))

        list1 = sorted(prefixGcd)

        low = 0
        high = n-1
        ans = 0
        while (low < high):
            ans += gcd(list1[low], list1[high])

            low += 1
            high -= 1

        return ans