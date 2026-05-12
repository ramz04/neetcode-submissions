class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            outputNum = 1
            for j in range(len(nums)):
                if i != j:
                    outputNum *= nums[j]
            output.append(outputNum)
        return output



                
                
                
        
        
        
            
                


        