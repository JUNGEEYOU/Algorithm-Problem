import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
visit = [False] * (n + 1)
arr.sort()
num = []
all_nums = set()

def recursion():
    if len(num) == m:
        x = set((map(int, num)))
        all_nums.add(x)
        return
    for i, a in enumerate(arr):
        if not visit[i]:
            num.append(a)
            visit[i] = True
            recursion()
            num.pop()
            visit[i] = False

recursion()

for nums in sorted(all_nums):
    print(*nums)

