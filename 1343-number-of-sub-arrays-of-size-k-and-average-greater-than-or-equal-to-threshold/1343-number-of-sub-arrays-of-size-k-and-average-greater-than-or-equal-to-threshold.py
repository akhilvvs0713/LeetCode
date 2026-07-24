class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res,l,total=0,0,0
        for i in range(len(arr)):
            total+=arr[i]
            if i-l+1 == k :
                if total/k >=threshold:
                    res+=1
                total -= arr[l]
                l+=1
        return res

