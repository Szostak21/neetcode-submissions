class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        pivot = 0

        def binarySearch(l,r):
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif target > nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
            return -1

        while l <= r:
            if nums[l] <= nums[r]:
                if nums[l] < nums[pivot]:
                    pivot = l
                break

            mid = (l+r)//2

            if nums[mid] < nums[pivot]:
                pivot = mid

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return max(binarySearch(0,pivot - 1), binarySearch(pivot,len(nums)-1))
