import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
visit = [False] * n
result = 11
for _ in range(n):
    _, b = map(str, sys.stdin.readline().split())
    arr.append(b)

def dfs(cnt):
    global result
    if cnt == n:   # 모든 기타의 유무를 표시한 경우
        song = [False] * m   # 곡에 대한 유무
        count = 0
        for i, v in enumerate(visit):
            if v:       # 만약 방문한 경우인 경우
                count += 1
                for j, a in enumerate(arr[i]):
                    if a == "Y":  # 만약 연주할수 있는 곡인 경우
                        song[j] = True
        flag = True
        for t in song:   # 모든 곡이 True인 경우를 확인
            if not t:
                flag = False
        if flag:     # 모든 곡이 true이면 최소값 등록
            result = min(result, count)
        return
    visit[cnt] = True
    dfs(cnt + 1)
    visit[cnt] = False
    dfs(cnt + 1)

dfs(0)
result = -1 if result == 11 else result
print(result)
