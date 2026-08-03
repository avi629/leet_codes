class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        dict = {height: name for height, name in zip(heights, names)}
        res = sorted(dict.keys())
        result = reversed(res)
        main_res = [dict[h] for h in result]
        return main_res