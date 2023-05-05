class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ind_a = 0
        for a in nums:
            ind_b = ind_a + 1
            for b in nums[ind_b:]:
                if a + b == target:
                    return [ind_a, ind_b]
                ind_b += 1
            ind_a += 1

print(Solution().twoSum([2,7,11,15], 22))
