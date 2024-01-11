class Solution:
    def removeDuplicates(self, nums):
        dt = {}
        for i in range(len(nums)):
            dt[i] = nums[i]
        print(dt)
x = Solution()
nums = [1, 1, 1, 2, 2, 3, 4, 4, 4]
x.removeDuplicates(nums)

