class Solution(object):
    def maxProfit(self, prices):
        l=0
        r=1
        m=0
        while r<len(prices):
            c=prices[r]-prices[l]
            if prices[l]<prices[r]:
                m=max(c,m)
            else:
                l=r
            r+=1
        return m