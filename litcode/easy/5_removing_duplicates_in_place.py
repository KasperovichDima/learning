# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the
# first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k
# (hence they are underscores).

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 0
        for _ in nums[1:]:
            if _ != nums[left]:
                left += 1
                nums[left] = _
        return left + 1


nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()
print(s.removeDuplicates(nums))
