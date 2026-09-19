class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)

        # Product of everything to the LEFT
        product = 1
        for i in range(len(nums)):
            res[i] = product
            product *= nums[i]

        # Product of everything to the RIGHT
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= product
            product *= nums[i]

        return res
        