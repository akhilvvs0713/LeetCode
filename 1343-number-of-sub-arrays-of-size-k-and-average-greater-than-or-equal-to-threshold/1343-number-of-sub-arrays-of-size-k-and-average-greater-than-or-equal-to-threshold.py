class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        res,l,total=0,0,0
        for r in range(len(arr)):
            total+=arr[r]
            if r-l+1 == k:
                if total / k >= threshold:
                    res+=1
                total-=arr[l]
                l+=1
        return res