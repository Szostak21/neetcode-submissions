class Solution:
    def productExceptSelf(self, nums: List(int)) -> List(int):
        n = len(nums)
        res = [1] * n

        #1,2,4,6
        #1,1,2,8
        #48,24,6,1
        #48,24,12,8


        for i in range(1,n):
            res[i] = res[i - 1] * nums[i -1]

        prefix = 1
        for i in range(n-2,-1,-1):
            prefix *= nums[i + 1]
            res[i] *= prefix

        return res
