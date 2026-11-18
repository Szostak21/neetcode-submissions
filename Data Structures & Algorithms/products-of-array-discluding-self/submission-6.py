class Solution:
    def productExceptSelf(self, nums: List(int)) -> List(int):
        n = len(nums)
        res = [1] * n

        # 1,2,4,6

        # 1,1,2,8   pref
        # 48,24,6,1 suff

        # 48,24,12,8

        for i in range(1,n):
            res[i] = res[i-1] * nums[i-1]

        suff = 1
        for j in range(n-2,-1,-1):
            suff *= nums[j+1]
            res[j] *= suff
        
        return res