import sys; sys.stdin = open("input.txt", "r")
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def willMeet(a, b):
    x1, x2, y1, y2 = a[0], b[0], a[1], b[1]
    dx1, dx2, dy1, dy2 = dx[a[2]], dx[b[2]], dy[a[2]], dy[b[2]]
    #1. 움직이는 방향이 가로만 존재하거나 세로만 존재하면 언젠가는 만남
    if dy1==dy2:
        if y1!=y2: return False
        if dx1==dx2: return False
        tx = (x2-x1)/(dx1-dx2)
        return tx if tx>0 else False

    if dx1==dx2:
        if x1!=x2: return False
        if dy1==dy2: return False
        ty = (y2-y1)/(dy1-dy2)
        return ty if ty > 0 else False

    #3. 움직이는 방향이 가/세 존재할때
    tx = (x2-x1)/(dx1-dx2)
    ty = (y2-y1)/(dy1-dy2)
    if tx<=0: return False
    if ty<=0: return False
    if tx!=ty: return False
    else: return tx


def appendElement(t, key, who):
    info[key] = [t, [who]]

def updateElement(t, key, who):
    ori = info[key]
    if ori[0] < t:
        return False
    if ori[0] == t:
        info[key][1].append(who)
        return True
    if ori[0] > t:
        info[key] = [t, [who]]
        return True

def update(a, b, t):
    if [a,b]==[1,2]:
        print(info, t)
    #key로 등록 안되어있으면 등록부터
    if (a not in info.keys()) and (b not in info.keys()):
        appendElement(t, a, b)
        appendElement(t, b, a)
        return
    if (a in info.keys()) and (b not in info.keys()):
        res = updateElement(t, a, b)
        if res: appendElement(t, b, a)
        return
    if (a not in info.keys()) and (b in info.keys()):
        res = updateElement(t, b, a)
        if res: appendElement(t, a, b)
        return
    if (a in info.keys()) and (b in info.keys()):
        res = updateElement(t, b, a)
        if res: updateElement(t, a, b)
        return
    
T = int(input())
for tc in range(1,T+1):
    info = dict()
    N = int(input())
    B = [list(map(int, input().split())) for i in range(N)]
    mm = [[-1]*N for _ in range(N)]#meet map

    #만나는 시간 맵 업데이트
    for i in range(N):
        for j in range(i+1, N):
            t = willMeet(B[i], B[j])
            if t: mm[i][j] = t

    power = 0
    for key in info:
        power += B[key][3]
    print(f"#{tc} {power}")

