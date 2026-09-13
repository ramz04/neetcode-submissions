class Solution:

    def encode(self, strs: List[str]) -> str:
        newArr = []
        for i in strs:
            newArr.append(f"{len(i)}#{i}")
        print(newArr)
        return "".join(newArr)





    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        newArr = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            newArr.append(s[start:end])
            i = end
        
        return newArr   


