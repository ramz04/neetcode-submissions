class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for i in nums:
            if i not in res:
                res[i] = 1
            res[i] += 1

        sorted_res = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))
        arr = list(sorted_res.keys())
        return arr[:k]