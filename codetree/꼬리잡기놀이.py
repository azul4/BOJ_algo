import sys; sys.stdin = open("input.txt", "r")

from collections import deque
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
route = arr[:][:]
dr=[0,-1,0,1]
dc=[1,0,-1,0]

#정답 변수
score = 0

#q = deque()
visited = [ [0]*n for i in range(n)]
def bfs(_r, _c):
    global arr
    visited[_r][_c] = 1
    q, myteam = deque(), deque()
    q.append([_r,_c])
    myteam.append([_r,_c])

    while q:
        [r, c] = q.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0>nr or nr>=n or 0>nc or nc>=n: continue #격자 내 존재
            if visited[nr][nc]: continue

            if arr[nr][nc] == 2: #이어지는사람
                visited[nr][nc]=1
                q.append([nr,nc])
                myteam.append([nr,nc])

                #if next is 3, push and return
                for j in range(4):
                    nnr, nnc = nr+dr[j], nc+dc[j]
                    if 0>nnr or nnr>=n or 0>nnc or nnc>=n: continue #격자 내 존재
                    if visited[nnr][nnc]: continue
                    if arr[nnr][nnc] == 3:
                        visited[nnr][nnc] = 1
                        myteam.append([nnr,nnc])
                        return myteam
    return myteam

def setRoute():
    for r in range(n):
        for c in range(n):
            if 1 <= route[r][c] <= 3:
                route[r][c] = 4

def setTeam():
    team = [deque() for _ in range(m)]
    i = 0
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 1 and not visited[r][c]:
                team[i] = bfs(r, c)
                i += 1
    return team

def moveForward(team):
    for i in range(m):
        t = team[i]
        hr, hc = t[0]
        for j in range(4):
            nr, nc = hr+dr[j], hc+dc[j]
            if 0<=nr<n and 0<=nc<n and [nr,nc] != t[1] and route[nr][nc]==4:
                team[i].pop()
                t.appendleft([nr,nc])
                break

def throwBall(round):
    sr, sc, dir = 0, 0, 0
    quo, res = (round-1)//n, round % n
    quo = quo % 4

    #시작 위치 sr, sc 정하기
    round2 = (round-1)%(4*n)
    if 0 <= round2 < n:
        sr, sc = round2, 0
    elif n <= round2 < 2*n:
        sr, sc = n-1, round2%n
    elif 2*n <= round2 < 3*n:
        sr, sc = n-1-(round2%n), n-1
    elif 3*n <= round2 < 4*n:
        sr, sc = 0, n-1-(round2%n)
    dir = quo
    return sr, sc, dir

def changeTeamDir(team, i):
    team[i].reverse()

def catchBall(sr, sc, dir, team):
    global score
    r, c = sr, sc
    didx = 0
    for i in range(n): #공 위치
        for tidx in range(m): # 최대 5개의 덱
            for curT in team[tidx]: #덱 하나 고르기
                if [r,c] == curT:
                    #print(f"{j}번째 위치")
                    score += (didx+1) ** 2
                    changeTeamDir(team, tidx)
                    return
                didx += 1
            didx = 0
        r, c = r+dr[dir], c+dc[dir]

team = setTeam()
setRoute()
for round in range(1,k+1):
    moveForward(team)
    sr, sc, dir = throwBall(round)
    catchBall(sr, sc, dir, team)
print(score)
