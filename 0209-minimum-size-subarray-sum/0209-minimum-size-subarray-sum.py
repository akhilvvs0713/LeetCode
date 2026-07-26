class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l=0
        window_sum=0
        ans=float("inf")
        for r in range(len(nums)):
            window_sum+=nums[r]
            while window_sum >= target:
                ans=min(ans,r-l+1)
                window_sum-=nums[l]
                l+=1
        return 0 if ans == float("inf") else ans