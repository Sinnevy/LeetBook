def insertion_sort(nums, n):

    for i in range(0, n):
        j = i
        while j>0 and nums[j] < nums[j-1]:
            temp = nums[j]
            nums[j] = nums[j-1]
            nums[j-1] = temp
            j -= 1


if __name__ == '__main__':

    nums = [1,0, 9, 7, 4, 5, 2]
    insertion_sort(nums , len(nums))

    print(nums)

