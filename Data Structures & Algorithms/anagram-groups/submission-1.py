class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for i in strs:
            hashKey = "".join(sorted(i))
            if hashKey not in hashMap:
                hashMap[hashKey] = [i]
            elif hashKey == "".join(sorted(i)):
                hashMap[hashKey].append(i)
        
        return list(hashMap.values())



        
        
        
            