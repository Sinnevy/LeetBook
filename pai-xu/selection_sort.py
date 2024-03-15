def selection_sort(nums, n):
    for i in range (0, n-1):
        mid = i
        for j in range (i+1, n):
            if nums[j] < nums[mid]:
                mid = j
        temp = nums[mid]
        nums[mid] = nums[i]
        nums[i] = temp



if __name__ == '__main__':
    nums = [1, 0, 9, 7, 4, 5, 2]
    selection_sort(nums,  len(nums))

    print(nums)