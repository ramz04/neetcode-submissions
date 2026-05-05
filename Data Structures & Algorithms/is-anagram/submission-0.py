from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = dict(Counter(s))
        dictT = dict(Counter(t))

        print(dictS, dictT)

        return dictS == dictT
        