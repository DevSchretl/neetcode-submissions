class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ltr = 1
        rtl = 1
        prods = [1] * len(nums)

        for i in range(len(nums)):
            prods[i] *= ltr
            ltr *= nums[i]
            prods[-i-1] *= rtl
            rtl *= nums[-i-1]

        return prods
