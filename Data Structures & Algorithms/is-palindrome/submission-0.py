class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        arrayS = []
        for item in s:
            if item.isalnum():
                arrayS.append(item)

        return arrayS == arrayS[::-1]

        
        
        


        