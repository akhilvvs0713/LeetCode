class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram=defaultdict(list)
        for i in strs:
            sor=''.join(sorted(i))
            anagram[sor].append(i)
        return list(anagram.values())