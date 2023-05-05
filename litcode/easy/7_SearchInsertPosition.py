class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        
        mid = len(nums) // 2
        while nums[mid] != target and 0 < mid < len(nums) -1:
            if nums[mid - 1] < target < nums[mid + 1]:
                return mid
            else:
                add = (mid // 2) if mid > 1 else 1
                mid += add if mid < target else -add
        return mid
        


nums = ([1,3,5,6], [1,3,5,6], [1,3,5,6], [1,3], [1,3])
vals = (5,2,7,0,2)
args = zip(nums, vals)
s = Solution()
# print(s.searchInsert([1,3], 0))
for _ in args:
    print(s.searchInsert(_[0], _[1]))

2
1
4
0
1