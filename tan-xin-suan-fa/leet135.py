def candy(ratings):
    size = len(ratings)
    if size < 2:
        return size
    
    # 初始化一个长度为i的数组 每个元素都是1
    num = [1 for _ in range(size)]

    for i in range(1, len(ratings), 1):
        if ratings[i] > ratings[i-1]:
            num[i] = num[i-1]+1

    for i in range(len(ratings)-1, 0, -1):
        if ratings[i] < ratings[i-1]:
            num[i-1] = max(num[i-1], num[i]+1)

    print(num)


if __name__ == '__main__':
    candy([1,0,2])

    print('——————————————————————————')
    for i in range(0, 9, 1):
        print(i)

    print('——————————————————————————')
    for i in range(9, 0, -1):
        print(i)