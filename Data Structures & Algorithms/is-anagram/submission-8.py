class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashT, hashS = {}, {}

        for i in t:
            if i not in hashT:
                hashT[i] = 1
            else:
                hashT[i] += 1

        for x in s:
            if x not in hashS:
                hashS[x] = 1
            else:
                hashS[x] += 1

        return hashT == hashS