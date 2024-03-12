# 有一群孩子和一堆饼干，每个孩子有一个饥饿度，每个饼干都有一个大小。每个孩子只能吃
# 一个饼干，且只有饼干的大小不小于孩子的饥饿度时，这个孩子才能吃饱。求解最多有多少孩子
# 可以吃饱。
def findContentChild(children, cookies):
    children.sort()
    cookies.sort()

    child = 0
    cookie = 0

    while child < len(children) and cookie < len(cookies):
        if children[child] <= cookies[cookie]:
            child += 1
        cookie += 1

    print(child)


if __name__ == '__main__':
    findContentChild([1,3,4,5], [1,2,3])

