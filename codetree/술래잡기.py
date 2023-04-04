import sys; sys.stdin = open("input.txt", "r")
n, m, h, k = map(int, input().split())

run = [list(map(int, input().split())) for _ in range(m)]
catch = [(n//2)+1, (n//2)+1]
tree = [list(map(int, input().split())) for _ in range(h)]

dr = [-1,0,1,0]
dc = [0,1,0,-1]  #상 우 하 좌 인덱스

hl = [i for i in range(1, 99)]  # helper list for catcher
for i in range(2, 98 * 2, 2):
    hl.insert(i,(i//2)+1)
hl.insert(0,1)
hl.append(99)
hld = [0,1,2,3] * 49 + [0]
opposite = False

def calcDist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def withinBound(r, c):
    return True if (0<r<=n and 0<c<=n) else False


def moveRunner(i):
    #run[i]이 도망가야함
    R = run[i]
    nr, nc = R[0] + dr[R[2]], R[1] + dc[R[2]]
    #print(f"nr, nc = {nr, nc}")
    if not withinBound(nr, nc):
        R[2] = (R[2] + 2) % 4 #방향 바꿔줌
        nr, nc = R[0] + dr[R[2]], R[1] + dc[R[2]]
        if [nr,nc] != catch:
            run[i] = [nr, nc, R[2]]
        else:
            pass # 술래와 같은 위치가 될 거면 움직이지 않음
    else:
        if [nr,nc] != catch:
            run[i] = [nr, nc, R[2]]
        else:
            pass # 술래와 같은 위치가 될 거면 움직이지 않음


def moveCatcher():
    pass



for round in range(1,k+1):
    #1. 도망자 도망감
    for i in range(m):
        if calcDist(run[i][:2], catch) <= 3:
            moveRunner(round)

    #2. 술래 달팽이모양으로 움직임
    moveCatcher()
