import sys; sys.stdin = open("input.txt", "r")
n, m, k = map(int, input().split())
fb = [list(map(int, input().split())) for _ in range(m)]
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]
#arr = [[list() for _ in range(n)] for _ in range(n)]
R, C, M, S, D = 0, 1, 2, 3, 4 #fb의 인덱스

def FbTask(ft, r, c): #2개이상의 파이어볼
    # 질량, 속력, 방향 세팅
    nm, ns, nd = 0, 0, [0,2,4,6]
    nfb = []

    # 질량 세팅
    for _fb in ft:
        nm += _fb[M]
    nm = nm//5

    #속력 세팅
    for _fb in ft:
        ns += _fb[S]
    ns //= len(ft)

    #방향 세팅
    flag = []
    for _fb in ft:
        if _fb[D] % 2 == 0:
            flag.append(True) # 짝수면 True 반환
    if len(flag) == len(ft) or len(flag) == 0: #모두 짝수또는 홀수라면
        nd = [0,2,4,6]
    else:
        nd = [1,3,5,7]
    if nm>0:
        for i in range(4):
            #nr = (ft[0][R] + dr[nd[i]] * _fb[S]) % n
            #nc = (ft[0][C] + dc[nd[i]] * _fb[S]) % n
            nfb.append([ft[0][R], ft[0][C],nm, ns, nd[i]])
    return nfb

def setFbOnArray(arr): #파이어볼 array로 옮기기
    for i in range(len(fb)):
        r, c = fb[i][R], fb[i][C]
        arr[r][c].append(fb[i]) #fb 자체를 넣음


def moveFireball():
    for i in range(len(fb)):
        cfb = fb[i] #현재 파이어볼

        nr = (cfb[R] + dr[cfb[D]] * cfb[S]) % n
        nc = (cfb[C] + dc[cfb[D]] * cfb[S]) % n
        fb[i][R], fb[i][C] = nr, nc

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
    arr = [[list() for _ in range(n)] for _ in range(n)] # arr 초기화
    moveFireball()
    #print("{}회차 움직이고 난 뒤".format(i))
    #print(fb)
    setFbOnArray(arr)
    #print(arr)
    for r in range(n):
        for c in range(n):
            if len(arr[r][c]) >= 2: #한 칸에 파이어볼이 2개 이상 있다면
                nfb = FbTask(arr[r][c], r, c) #파이어볼 작업 시작
                #기존 파이어볼 삭제
                for _ofb in arr[r][c]:
                    fb.remove(_ofb)
                #신규 파이어볼 추가
                for _nfb in nfb:
                    fb.append(_nfb)

    #print("{}회차 끝:".format(i))
    #print(fb)

print(getLastFireballMass())

