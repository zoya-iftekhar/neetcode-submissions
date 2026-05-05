class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and target - nums[j] == nums[i]:
                    return sorted([i, j])