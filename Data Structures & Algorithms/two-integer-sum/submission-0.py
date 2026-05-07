class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i, j in enumerate(nums):
            diff = target - j
            if diff in nums[i + 1:]:
                arr.append(i)
                arr.append(nums.index(diff, i + 1))
                return arr
        
        print(arr)

        return arr

        