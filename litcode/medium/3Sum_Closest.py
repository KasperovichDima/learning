"""
Given an integer array nums of length n and an integer target, find three integers in
nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

 

Constraints:

    3 <= nums.length <= 500
    -1000 <= nums[i] <= 1000
    -104 <= target <= 104


"""
from collections import deque


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        differences: deque[int] = deque(maxlen=3)
        diff = abs(target - sum(nums[:3]))
        for num in nums[3:]:
            differences.append(abs(target - num - sum(nums[1:3])))
            differences.append(abs(target - sum((nums[0], num, nums[2]))))
            differences.append(abs(target - sum(nums[:2]) - num))
            if (min_diff := abs(min(differences))) < diff:
                nums[differences.index(min_diff)] = num
                diff = min_diff
        return sum(nums[:3])
    

s = Solution()

cases = (
    # ([-1,2,1,-4], 1),
    # ([0,0,0], 1),
    # ([6,-8,3,-5,0], 15),
    # ([1,1,1,0], -100),
    (
    [321,413,82,812,-646,-858,729,609,-339,483,-323,-399,-82,-455,18,661,890,-328,-311,
     520,-865,-174,55,685,-636,462,-172,-696,-296,-832,766,-808,-763,853,482,411,703,655,
     -793,-121,-726,105,-966,-471,612,551,-257,836,-94,-213,511,317,-293,279,-571,242,
     -519,386,-670,-806,-612,-433,-481,794,712,378,-325,-564,477,169,601,971,-300,-431,
     -152,285,-899,978,-419,708,536,-816,-335,284,384,-922,-941,633,934,497,-351,62,392,
     -493,-44,-400,646,-912,-864,835,713,-12,322,-228,340,-42,-307,-580,-802,-914,-142,
     575,-684,-415,718,-579,759,579,732,-645,525,114,-880,-603,-699,-101,-738,-887,327,
     192,747,-614,393,97,-569,160,782,-69,235,-598,-116,928,-805,-76,-521,671,417,600,
     -442,236,831,637,-562,613,-705,-158,-237,-299,808,-734,364,919,251,-163,-343,899],
     2218
    ),
)

for case in cases:
    res = s.threeSumClosest(*case)
    print(res)
