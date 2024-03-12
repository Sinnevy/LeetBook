def merge1(nums1, m, nums2, n):
    for i in range(0, n, 1):
        nums1[m+i] = nums2[i]
    b = sorted(nums1)
    # sort()方法修改原数组；sorted函数创建新数组
    print(b)
    print('——————————————————————————')
    print(nums1)


def merge2(nums1, m, nums2, n):
    for i in range(0, n, 1):
        nums1[m+i] = nums2[i]
    nums1.sort()
    print(nums1)


if __name__ == '__main__':
    merge1( [1,2,3,0,0,0], 3,  [2,5,6], 3)