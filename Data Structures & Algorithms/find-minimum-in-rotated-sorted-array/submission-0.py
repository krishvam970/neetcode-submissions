class Solution:
    def findMin(self, nums: List[int]) -> int:
        minu = nums[0]
        for i in range(len(nums)):
            if nums[i]<minu:
                minu=nums[i]
        return minu
