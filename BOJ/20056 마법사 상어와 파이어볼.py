#import sys; sys.stdin = open("input.txt", "r")
n, m, k = map(int, input().split())
fb = [list(map(int, input().split())) for _ in range(m)]
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]
MAP = [[list() for _ in range(n)] for _ in range(n)]  # arr 초기화

#arr = [[list() for _ in range(n)] for _ in range(n)]
R, C, M, S, D = 0, 1, 2, 3, 4 #fb의 인덱스

def FbTask(ft, r, c): #2개이상의 파이어볼
    # 질량, 속력, 방향 세팅
    #nfb = []
    flag = []
    cnt = len(MAP[r][c])
    nm, ns, nd = 0, 0, [0, 2, 4, 6]
    while ft:
        _m, _s, _d = ft.pop(0)
        nm += _m
        ns += _s

        #방향 세팅
        if _d % 2 == 0:
            flag.append(True) # 짝수면 True 반환
    if len(flag) == cnt or len(flag) == 0: #모두 짝수또는 홀수라면
        nd = [0,2,4,6]
    else:
        nd = [1,3,5,7]
    if nm//5>0:
        for i in range(4):
            fb.append([r, c, nm//5, ns//cnt, nd[i]])
    #return nfb



def moveFireball():
    while fb:
        r, c, m, s, d = fb.pop(0)
        r = (r + dr[d] * s) % n
        c = (c + dc[d] * s) % n
        MAP[r][c].append([m,s,d])

def init(): #fb의 R, C를 모두 -1, -1씩 becuz (1,1) 오프셋 되어있으니까.
    for i in range(m):
        fb[i][R] -=1
        fb[i][C] -=1

def getLastFireballMass():
    mass = 0
    for _m in fb:
        mass += _m[M]
    return mass


init()
for i in range(k):
    moveFireball()
    for r in range(n):
        for c in range(n):
            if len(MAP[r][c]) >= 2: #한 칸에 파이어볼이 2개 이상 있다면
                #MAP[r][c] = \
                FbTask(MAP[r][c], r, c) #파이어볼 작업 시작
                #for _ in MAP[r][c]: fb.append([r,c]+_)
            if len(MAP[r][c]) == 1:
                fb.append([r,c] + MAP[r][c].pop(0))



print(sum([f[2] for f in fb]))

