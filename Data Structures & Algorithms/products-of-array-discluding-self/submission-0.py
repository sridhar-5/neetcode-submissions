class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        prefix_product = 1
        for i in range(1, len(nums)):
            prefix_product *= nums[i-1]
            prefix.append(prefix_product)
        
        suffix = [1]
        suffix_product = 1
        for i in range(len(nums) - 1, 0, -1):
            suffix_product *= nums[i]
            suffix.append(suffix_product)
        
        suffix.reverse()

        output =[]
        for i in range(len(nums)):
            output.append(prefix[i] * suffix[i])
        
        return output


