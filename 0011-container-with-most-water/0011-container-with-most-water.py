class Solution:
    def maxArea(self, height: List[int]) -> int:
        r=len(height)-1
        l=m=0
        while l < r:
            h=min(height[l],height[r])
            w=r-l
            area=h*w
            m=max(area,m)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return m

