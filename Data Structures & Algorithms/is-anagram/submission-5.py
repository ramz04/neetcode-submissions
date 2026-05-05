class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}
        
        for x in s:
            count_s[x] = count_s.get(x, 0) + 1
        
        for y in t:
            count_t[y] = count_t.get(y, 0) + 1

        return count_s == count_t

        