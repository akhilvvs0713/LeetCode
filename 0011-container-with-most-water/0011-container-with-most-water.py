class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        r=len(height)-1
        l=0
        ans=0
        while l < r:
            h=min(height[l],height[r])
            w=r-l
            area=h*w
            ans=max(ans,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return ans