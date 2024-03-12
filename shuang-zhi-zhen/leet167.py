def twoSum(nums, target):
    l = 0
    r = len(nums)-1
    while l < r:
        summary = nums[l] + nums[r]
        if summary == target:
            break
        if summary < target:
            l += 1
        else:
            r -= 1

    return print(str(l) + ' ' + str(r))


if __name__ == '__main__':

    twoSum([2,7,11,15], 22)