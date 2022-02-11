def find_error_nums(nums):
    nums.sort()
    total_length = len(nums)
    val = 1
    final_list = []
    if len(nums) == 1:
        return []

    nums.insert(0,0)
    while val < total_length:
        if nums[val] == nums[val +1] and  nums[val-1] < nums[val] and nums[1] > 1:
            final_list.append(nums[val])
            final_list.append(nums[val]-1)
            nums[val] = nums[val] - 1
        elif nums[val] == nums[val +1]:
            final_list.append(nums[val])
            final_list.append(nums[val] +1)
            nums[val+1] = nums[val] + 1

        val = val + 1

    return final_list

    
print(find_error_nums([1,1]))