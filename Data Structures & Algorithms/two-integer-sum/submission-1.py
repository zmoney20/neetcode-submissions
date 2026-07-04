class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in indices:
                return [indices[difference], index]
            indices[num] = index
        return []