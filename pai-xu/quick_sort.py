def quick_sort(nums, l, r):
    if l+1 > r:
        return
    first, last  = l, r-1
    key = nums[first]
    while first < last:
        while first < last and nums[last] >= key:
            last -= 1
        nums[first] = nums[last]
        while first < last and nums[first] <= key:
            first += 1
        nums[last] = nums[first]

    nums[first] = key
    quick_sort(nums, l, first)
    quick_sort(nums, first+1, r)


if __name__ == '__main__':

    nums = [1,0, 9, 7, 4, 5, 2]
    quick_sort(nums, 0 , len(nums))
    print(nums)