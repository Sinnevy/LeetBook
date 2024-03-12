def judgeSquareSum(c):
    r = 0
    while r*r < c:
        r += 1
    l = 0

    while l < r:
        if l*l + r*r == c:
            break
        if l*l + r*r < c:
            l += 1
        else:
            r -= 1

    if l*l + r*r == c:
        print(str(l) + " " + str(r))
    else:
        print('false')

if __name__ == '__main__':

    judgeSquareSum(25)