class Solution:

    def encode(self, strs: List[str]) -> str:
        newStr = ""

        for i in strs:
            newStr += f"{len(i)}#{i}"
        return newStr
        
    def decode(self, s: str) -> List[str]:
        newArr = []
        i = 0
        while i < len(s):
            hashIndex = s.index("#", i)
            strLen = int(s[i: hashIndex])
            newArr.append(s[hashIndex + 1 : hashIndex + 1 + strLen])
            i = hashIndex + 1 + strLen
        return newArr
        

        
