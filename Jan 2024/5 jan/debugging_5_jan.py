import bisect

class Solution:
    def lengthOfLIS(self, nums):
        lis = []
        res = 1;
        for i in range(0,len(nums)):
            j = bisect.bisect_left(lis,nums[i]);
            if(j<len(lis)): 
                lis[j] = nums[i]
            else:
                lis.append(nums[i])
            if(len(lis)>res):
                res = len(lis)
        return res

nums = [10,9,2,5,3,7,101,18]
x = Solution()
print(x.lengthOfLIS(nums))