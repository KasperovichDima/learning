class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        res_lst = sorted(nums1 + nums2)
        mid_ind, rest = divmod(len(res_lst), 2)
        mid_ind -= 1
        if rest:
            return res_lst[mid_ind + 1]
        else:
            return sum((res_lst[mid_ind], res_lst[mid_ind + 1])) / 2


    

s = Solution()
cases = (
    ([1, 2], [3, 4]),
    ([1, 3], [2]),
    ([], [1,2,3]),
)
for case in cases:
    print(s.findMedianSortedArrays(*case))