class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        hashSet = set(nums)

        for i in hashSet:
            if (i - 1) not in hashSet:
                len = 1
                while (i + len) in hashSet:
                    len += 1
                count = max(len, count)
        
        return count
