class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newArr = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            newArr[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums) -1, -1, -1):
            newArr[i] *= suffix
            suffix *= nums[i]
        
        return newArr






        