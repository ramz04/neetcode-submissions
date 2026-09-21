class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS, hashT = {}, {}

        for i in s:
            if i not in hashS:
                hashS[i] = 1
            else:
                hashS[i] += 1
        
        for x in t:
            if x not in hashT:
                hashT[x] = 1
            else:
                hashT[x] += 1

        return hashS == hashT
