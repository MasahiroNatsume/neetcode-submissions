class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            num_2 = target - num
            if num_2 in seen:
                return [seen[num_2], i]
            seen[num] = i
        return []