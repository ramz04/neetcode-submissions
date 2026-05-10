class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for i in strs:
            encodedStr += f"{len(i)}#{i}"
        print(encodedStr)
        return encodedStr

    def decode(self, s: str) -> List[str]:
        decodedArr = []
        x = 0

        while x < len(s):
            j = s.index('#', x)
            length = int(s[x:j])
            decodedArr.append(s[j + 1: j+1+length])
            x = j + 1 + length
        return decodedArr


        
