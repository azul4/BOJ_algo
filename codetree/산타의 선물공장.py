import sys; sys.stdin=open("input.txt", "r")

HEAD = [-1 for _ in range(10)] #rail 기준
TAIL = [-1 for _ in range(10)]#rail 기준
NXT = dict()# [-1 for _ in range(1000010)]#ID 기준, append방식으로
PRV = dict()#[-1 for _ in range(1000010)]#ID 기준, append방식으로
IDS = dict() #IDS[ID번호] = 벨트번호, -1은 사라졌단거
good = [False for i in range(10)]
BOX = [[] for _ in range(10)]  # 박스의 id 집합


def debug():
    print(f"head={HEAD}")
    print(f"tail={TAIL}")
    print(f"next={NXT}")
    print(f"prev={PRV}")
    print(f"IDs={IDS}")

def cmd100(cmd): #공장설립
    n, m, info = cmd[0], cmd[1], cmd[2:]
    rail = 0
    for i in range(len(info)//2): #박스 개수만큼
        id, w = info[i], info[i+n]
        BOX[rail].append([id,w])
        IDS[id] = rail
        if i%4==3 and i>=3: rail+=1 #여기 4 바꿔줘야함


    #head, tail 정하기
    for i in range(m):
        HEAD[i], TAIL[i] = BOX[i][0][0], BOX[i][-1][0]
    #nxt, prv 정하기
    for i in range(m):
        for j in range(len(BOX[i]) - 1):
            NXT[BOX[i][j][0]] = BOX[i][j+1][0]
            PRV[BOX[i][j+1][0]] = BOX[i][j][0]
        #맨앞원소 prv=-1, 맨뒤원소 nxt=-1
        for j in range(len(BOX[i])):
            PRV[BOX[i][0][0]] = -1
            NXT[BOX[i][-1][0]] = -1
    #동작하는 라인 설정
    len(info) // 2
    for i in range(m):
        good[i] = True


def cmd200(w_max): #물건 하차
    global HEAD, TAIL, NXT, PRV, BOX
    score = 0
    w_max = int(w_max[0])
    for i in range(len(BOX)):
        if not len(BOX[i]): continue
        b = BOX[i].pop(0)
        if b[1] <= w_max: #하차 진행
            #원래 연결관계만 끊어주면 됨
            score += b[1]
            HEAD[i] = BOX[i][0][0]
            PRV[BOX[i][0][0]] = -1
            IDS[b[0]] = -1
            del PRV[b[0]], NXT[b[0]]
        else: #맨 뒤로 보내기
            #연결관계 바꿔주기
            BOX[i].append(b)
            HEAD[i], TAIL[i] = BOX[i][0][0], BOX[i][-1][0]
            NXT[BOX[i][0][0]] = BOX[i][1][0]
            PRV[BOX[i][0][0]] = -1
            NXT[BOX[i][-2][0]] = BOX[i][-1][0]
            PRV[BOX[i][-1][0]] = BOX[i][-2][0]
    print(score)


def cmd300(r_id): #물건 제거
    r_id = int(r_id[0])
    try:
        belt = IDS[r_id]
    except:
        print(-1)
        return
    for i in range(len(BOX[belt])):
        if r_id == BOX[belt][i][0]:
            break
    nnxt, nprv = NXT[r_id], PRV[r_id]
    NXT[nprv] = nnxt
    PRV[nnxt] = nprv
    IDS[r_id] = NXT[r_id] = PRV[r_id] = -1
    del BOX[belt][i]

    #헤드 테일 재정리
    HEAD[belt] = BOX[belt][0][0]
    TAIL[belt] = BOX[belt][-1][0]
    print(r_id)

def cmd400(f_id): #물건 확인
    f_id = int(f_id[0])
    try:
        belt = IDS[f_id]
        if belt==-1:
            print(-1)
            return
    except:
        print(-1)
        return

    for i in range(len(BOX[belt])):
        if f_id == BOX[belt][i][0]:
            break
    ot = BOX[belt][-1][0]
    om = BOX[belt][i][0]
    oh = BOX[belt][0][0]

    nh = om
    nt = PRV[om]
    NXT[nt] = -1
    NXT[ot] = oh
    PRV[nh] = -1
    PRV[oh] = ot

    HEAD[belt], TAIL[belt] = nh, nt
    BOX[belt] = BOX[belt][i:] + BOX[belt][0:i]
    print(i+1)

def cmd500(b_num): #라인 고장
    b_num = int(b_num[0])-1
    if not good[b_num]:
        print(-1)
        return
    good[b_num] = False
    li = [i for i in range(b_num, 10)] + [i for i in range(0, b_num)]
    mv = -1

    for i in range(10):
        if good[li[i]]:
            mv = li[i]
            break

    NXT[mv] = HEAD[b_num]
    PRV[b_num] = TAIL[mv]
    TAIL[mv] = TAIL[b_num]
    BOX[mv] += BOX[b_num]
    for elem in BOX[b_num]:
        IDS[elem[0]] = mv

    BOX[b_num] = []
    good[b_num] = False
    print(b_num+1)


q = int(input())
for _ in range(q):
    ord = list(map(int, input().split()))
    print(ord)
    if ord[0] == 100: cmd100(ord[1:])
    if ord[0] == 200: cmd200(ord[1:])
    if ord[0] == 300: cmd300(ord[1:])
    if ord[0] == 400: cmd400(ord[1:])
    if ord[0] == 500: cmd500(ord[1:])


#BOX로 풀면 OOM나서 안됨
#링크드 리스트를 쓰는 이유는 메모리 절약용 + 시간절약용