def removeDuplicates(nums):
    count = 0
    for i in range(len(nums) - 1):
        # rem = 0
        j = 0
        while nums[j] == nums[j+1]:
            print("j ",j)
            if count == 3:
                print('count', count)
                nums.remove(nums[j])
                nums.append('-')
            print(nums)
            count += 1
            j+=1
        count = 0
    print(nums)

    num = 0
    for i in range(len(nums)):
        if nums[i] != '_':
            num += 1 
    print(nums)
nums = [0,0,1,1,1,1,2,3,3]
# nums = [1,1,1,2,2,3]
res = removeDuplicates(nums)
# [0,0,1,1,2,3,3]
print(res)