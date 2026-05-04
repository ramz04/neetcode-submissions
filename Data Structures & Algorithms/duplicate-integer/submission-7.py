class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSet = set(nums)

        numsArray = []
        
        for i in numsSet:
            if i in nums:
                numsArray.append(i)

        return len(numsArray) != len(nums)
        