class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        m=-1
        i=len(arr)-1
        while i >= 0:
            temp=arr[i]
            arr[i]=m
            if temp>m:
                m=temp
            i-=1
        return arr