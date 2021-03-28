import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
num = []

def recursion():
    if len(num) == m:
        print(*num)
        return
    for i in arr:
        if i not in num:
            num.append(i)
            recursion()
            num.pop()

recursion()

