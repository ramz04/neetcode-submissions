class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 1
            else:
                hashMap[nums[i]] += 1
        
        sortedArr = sorted(hashMap, key=hashMap.get, reverse=True)

        return sortedArr[0:k]
        