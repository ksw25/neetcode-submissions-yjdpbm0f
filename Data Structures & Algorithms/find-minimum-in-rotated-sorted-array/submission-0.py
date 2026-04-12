class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest = 1001

        l, r = 0, len(nums)-1

        while l<=r:

            mid = (l+r)//2

            if nums[l]<=nums[mid]:
                smallest= min(smallest, nums[l])
                l = mid + 1
            else:
                smallest= min(smallest, nums[mid])
                r = mid - 1
        
        return smallest