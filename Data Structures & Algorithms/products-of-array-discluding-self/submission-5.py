class Solution:
    def productExceptSelf(self, nums: List(int)) -> List(int):
        n = len(nums)
        pref = [1] * n
        suff = [1] * n


        # 1,2,4,6

        # 1,1,2,8   pref
        # 48,24,6,1 suff

        # 48,24,12,8

        for i in range(1,n):
            pref[i] = pref[i-1] * nums[i-1]

        for j in range(n-2,-1,-1):
            suff[j] = suff[j+1] * nums[j+1]

        return [pref[i]*suff[i] for i in range(n)]
