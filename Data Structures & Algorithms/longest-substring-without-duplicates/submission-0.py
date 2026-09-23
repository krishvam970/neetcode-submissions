class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        maxl=0
        char=set()
        for r in range(len(s)):
            while s[r] in char:
                char.remove(s[l])
                l=l+1
            char.add(s[r])
            maxl=max(maxl,r-l+1)
        return maxl
        