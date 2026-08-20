class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, val in enumerate(nums):
            if val in dic:
                return [dic[val], i]
            dic[target-val] = i
