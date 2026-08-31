class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        while True:
            if len(nums) <= 2:
                return min(nums)

            mid = len(nums) // 2

            if nums[len(nums)-1] > nums[mid]:
                nums = nums[:mid+1]
            else:
                nums = nums[mid:]