class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        sorted_map = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))

        res = list(sorted_map.keys())

        return res[:k]