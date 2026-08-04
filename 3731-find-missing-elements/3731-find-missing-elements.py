class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        num_set=set(nums)
        a=[]
        for i in range(min(nums),max(nums)):
            if i not in num_set:
                a.append(i)
        return a