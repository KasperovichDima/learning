class Solution:
    def maxArea(self, height: list[int]) -> int:
        maximum = 0
        for outer_ind in range(len(height)):
            for inner_ind in range(len(height)):
                if (candidate := abs(outer_ind - inner_ind)
                    * min(height[outer_ind], height[inner_ind])) > maximum:
                    maximum = candidate

        return maximum


s = Solution()

print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(s.maxArea([1, 1]))
