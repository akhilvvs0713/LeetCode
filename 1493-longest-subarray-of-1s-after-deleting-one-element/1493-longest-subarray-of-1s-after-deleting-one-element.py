class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        l,z,a=0,0,0
        for r in range(n):
            if nums[r]==0:
                z+=1
            while z>1:
                if nums[l]==0:
                    z-=1
                l+=1
            a=max(a,r-l+1-z)
        return a-1 if a==n else a