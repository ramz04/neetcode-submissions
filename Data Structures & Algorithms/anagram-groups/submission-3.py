class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for i in strs:
            sortedString = "".join(sorted(i))

            if sortedString not in hashMap:
                hashMap[sortedString] = [] 
            hashMap[sortedString].append(i)
        
        return list(hashMap.values())
            


