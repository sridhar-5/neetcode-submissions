class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in sum_map:
                return [sum_map[complement], i]
            else:
                sum_map[nums[i]] = i