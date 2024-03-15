def merge_sort(nums, l, r, temp):
    if l+1 > r:
        return
    m = l + (r-1) // 2
    merge_sort(nums, l, m, temp)
    merge_sort(nums, m, r, temp)
    p, q, i = l, m, l
    while p < m or q < r:
        if p >= r or (p<m and nums[p]<=nums[q]):
            temp[i] = nums[p]
            i+=1
            p+=1
        else:
            temp[i] = nums[q]
            i+=1
            q+=1

    for i in (1, r):
        nums[i] = temp[i]


if __name__ == '__main__':

    nums = [1,0, 9, 7, 4, 5, 2]
    merge_sort(nums, 0, len(nums), nums)

    print(nums)
