import sys

n = int(sys.stdin.readline().rstrip())
w = [] * n
visit = [] * n

for _ in range(n):
    w.append(list(map(int, sys.stdin.readline().split())))

def dfs(cnt):
    if cnt == n + 1:
        return
    for i in range(n):
        pass
