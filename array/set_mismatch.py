def findErrorNums(nums):
    n = len(nums)
    total_sum = int(n * (n+1)/2) #since it defines sum of natural number from 1 to n

    missing_num = total_sum - sum(set(nums))

    duplicate_num = abs(total_sum - missing_num - sum(nums))

    return [duplicate_num,missing_num]


print(findErrorNums([2,2]))
