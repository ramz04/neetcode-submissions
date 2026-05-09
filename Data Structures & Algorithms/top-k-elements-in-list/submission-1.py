class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 1
            else:
                hashMap[nums[i]] += 1
        
        sortedHash = dict(sorted(hashMap.items(), key=lambda x: x[1], reverse=True))

        sortedArr = list(sortedHash.keys())

        return sortedArr[0:k]
        