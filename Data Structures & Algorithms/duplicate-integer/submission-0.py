class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        item_set = set()

        for number in nums:
            item_set.add(number)
        
        return not len(item_set) == len(nums)