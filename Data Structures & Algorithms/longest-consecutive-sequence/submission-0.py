class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookUp = set(nums)
        longest = 0


        for num in nums:

            if num-1 not in lookUp:
                largest =1

                while num+largest in lookUp:
                    largest+=1

                longest = max(longest, largest)
        return longest