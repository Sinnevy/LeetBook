# def validPalindrome(s):
#     def checkPalindrome(low, high):
#         l, r = 0, len(s)
#         while l < r:
#             if s[l] != s[r]:
#                 return False
#             l += 1
#             r -= 1
#         return True
#
#     low = 0
#     high = len(s)-1
#     while low < high:
#         if s[low] == s[high]:
#             low += 1
#             high -= 1
#         else:
#             return checkPalindrome(low+1, high) or checkPalindrome(low, high-1)
#
#     return True


def checkPalindrome(s, low, high):
    l, r = low, high
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def validPalindrome(s):
    low = 0
    high = len(s) - 1
    while low < high:
        if s[low] == s[high]:
            low += 1
            high -= 1
        else:
            return checkPalindrome(s, low + 1, high) or checkPalindrome(s, low, high - 1)

    return True


if __name__ == '__main__':
    print(validPalindrome('abicsisba'))
