def mySqrt(a):
    i = 0
    while i * i <= a:
        i += 1
    return i - 1


def mySqrt1(x):
    l, r, ans = 0, x, -1
    while l <= r:
        mid = (l + r) // 2
        if mid * mid <= x:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans


if __name__ == '__main__':
    print(mySqrt1(9))
