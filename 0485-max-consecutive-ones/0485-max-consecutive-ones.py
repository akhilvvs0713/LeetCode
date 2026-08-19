class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        coun=0
        for i in nums:
            if i==0:
                coun=0
            else:
                coun+=1
            if res<coun:
                res=coun
        return res