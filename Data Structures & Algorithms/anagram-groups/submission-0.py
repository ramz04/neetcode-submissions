class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for i in strs:
            hashKey = "".join(sorted(i))
            if hashKey not in hashMap:
                hashMap[hashKey] = [i]
            elif hashKey == "".join(sorted(i)):
                hashMap[hashKey].append(i)
        
        print(hashKey, hashMap, list(hashMap.values()))
        return list(hashMap.values())



        
        
        
            