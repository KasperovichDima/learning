# Ex1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Ex2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]


s = Solution()
# s.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# s.merge(nums1 = [1], m = 1, nums2 = [], n = 0)
# s.merge(nums1 = [0], m = 0, nums2 = [1], n = 1)
s.merge([4,0,0,0,0,0], 1, [1,2,3,5,6], 5)
# s.merge([1,2,4,5,6,0], 5, [3], 1)
[1,2,4,5,6,0]
[3]

[4,0,0,0,0,0]
[1,2,3,5,6]

[1,2,3,0,0,0]
[2,5,6]
