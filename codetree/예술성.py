from collections import deque
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
score = 0
dr = [-1,0,1,0] #시계방향
dc = [0,1,0,-1] #시계방향
group_arr = [[0]*n for _ in range(n)]

def debug():
    print(f"score = {score}")
    print("arr")
    for _ in arr: print(_)

########################### # 1.예술 점수 구하기 ##############################
def getGroup(visited, _r, _c, group_cnt):
    global group_arr
    #group_arr = [[0] * n for _ in range(n)]
    gs = 1
    q = deque()
    q.append([_r, _c])
    visited[_r][_c] = 1
    group_arr[_r][_c] = group_cnt
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]

            if 0>nr or nr>= n or 0>nc or nc>=n:  continue
            if visited[nr][nc]: continue
            if arr[nr][nc] != arr[_r][_c]: continue
            q.append([nr,nc])
            visited[nr][nc] = 1
            gs += 1
            group_arr[nr][nc] = group_cnt
    return [arr[_r][_c], gs, [_r, _c]]

def setAdjMatrix(group):
    size = len(group)
    al = [[0] * size for _ in range(size)]
    for r in range(n):
        for c in range(n): #0:n 0:n 전구간에 대하여
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if 0 > nr or nr >= n or 0 > nc or nc >= n:  continue
                if group_arr[nr][nc] == group_arr[r][c]: continue
                fr, to = group_arr[r][c], group_arr[nr][nc]
                al[fr][to] += 1
    return al


def getScore():
    global score
    # (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수 )
    #  x 그룹 a를 이루고 있는 숫자 값 x 그룹 b를 이루고 있는 숫자 값
    #  x 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수
    group = list()
    visited = [[0]*n for _ in range(n)]
    group_cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                li = getGroup(visited, i, j, group_cnt)
                group_cnt += 1
                group.append(li) #[group_val, group_size, [시작r,시작c]] 집합
    #al = [[0]*n for _ in range(n)] # 인접하는 변
    al = setAdjMatrix(group)

    for i in range(len(group)):
        for j in range(i+1, len(group)):
            each_score = (group[i][1] + group[j][1]) * group[i][0] * group[j][0] * al[i][j]
            score += each_score



############################ 2. 돌리기 ##############################
def rotateMiddle():
    mid = n//2
    for _ in range(3): # 십자 모양 반시계 90도 == 시계 90도*3번
        for i in range(1, (n//2)+1):
            temp = arr[mid + dr[3] * i][mid + dc[3] * i]
            arr[mid + dr[3] * i][mid + dc[3] * i] = arr[mid + dr[2] * i][mid + dc[2] * i]
            arr[mid + dr[2] * i][mid + dc[2] * i] = arr[mid+dr[1]*i][mid+dc[1]*i]
            arr[mid + dr[1] * i][mid + dc[1] * i] = arr[mid+dr[0]*i][mid+dc[0]*i]
            arr[mid + dr[0] * i][mid + dc[0] * i] = temp


def rotateSubArr(sr, er, sc, ec):
    #global arr
    subarr = list()
    temp = list()
    for i in range(sr, er+1):
        for j in range(sc, ec+1):
            temp.append(arr[i][j])
        subarr.append(temp)
        temp=list()
    size = len(subarr)
    for i in range(size):
        for j in range(size):
            arr[sr+i][sc+j] = subarr[size-j-1][i]

def rotate():
    rotateMiddle()
    rotateSubArr(0, n // 2 - 1, 0, n // 2 - 1)
    rotateSubArr(0, n // 2 - 1, n // 2 + 1, n-1)
    rotateSubArr(n // 2 + 1, n-1, 0, n // 2 - 1)
    rotateSubArr(n // 2 + 1, n-1, n // 2 + 1, n-1)

def init():
    global group_arr
    group_arr = [[0] * n for _ in range(n)]

getScore()
for _ in range(3):
    rotate()
    init()
    getScore()
print(score)
