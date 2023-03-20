import sys
#==================================
sys.stdin = open("input.txt", "r")
MAX_M, MAX_N = 100000,100000
prv, nxt = [-1] * (MAX_M+1), [-1]*(MAX_M+1)
head, tail, num_gift = [-1]*(MAX_N+1),[-1]*(MAX_N+1),[0]*(MAX_N+1)
factory=[]
def debug(n=4, m=9):
    print(f"prv = {prv[:m+1]}")
    print(f"nxt = {nxt[:m+1]}")
    print(f"head={head[:n+1]}")
    print(f"tail={tail[:n+1]}")
    print(f"num_gift={num_gift[:n+1]}")

def build_100(cmd):
    n, m, b_num = cmd[0], cmd[1], cmd[2:]
    factory = [[] for _ in range(n+1)]
    for (i, stuff) in enumerate(b_num):
        factory[stuff].append(i+1)
    
    for i in range(1,n+1):
        if len(factory[i])==0: continue
        head[i] = factory[i][0]
        tail[i] = factory[i][-1]
        num_gift[i] = len(factory[i])
        for j in range(len(factory[i])-1):
            nxt[factory[i][j]] = factory[i][j+1]
            prv[factory[i][j+1]] = factory[i][j]
    #debug(n, m)

def moveall_200(cmd):
    m_src, m_dst = cmd[0], cmd[1]

    #상자 연결구조 옮기기
    if num_gift[m_src] == 0:
        print(num_gift[m_dst])
        return
    if num_gift[m_dst] == 0:
        head[m_dst] = head[m_src]
        tail[m_dst] = tail[m_src]
        head[m_src] = -1
        tail[m_src] = -1
    else: # 양쪽 다 있을 경우
        #연결 관계 갱신
        ori_head = head[m_dst]
        src_tail = tail[m_src]
        nxt[src_tail] = ori_head
        prv[ori_head] = src_tail 

        #머리/꼬리 갱신
        head[m_dst] = head[m_src]
        tail[m_dst] = tail[m_dst]
        head[m_src] = -1
        tail[m_src] = -1
    
    #상자 개수 갱신
    num_gift[m_dst] += num_gift[m_src]
    num_gift[m_src] = 0 
    
    print(num_gift[m_dst])


def pop_head(li):
    #비어있으면 -1 리턴
    if not num_gift[li]:
        return -1
    #비어있지 않으면 head 리턴하면서 연결관계 끊어주기
    else:
        ori_head = head[li] #ori_head = 8
        # head[li] = nxt[ori_head] #head[3] = nxt[8] => head[3] = 9
        # nxt[ori_head] = -1 #nxt[8] = -1
        # prv[nxt[ori_head]] = -1 #prv[nxt[8]]
        head[li], nxt[ori_head], prv[nxt[ori_head]] = nxt[ori_head], -1, -1
        num_gift[li]-=1

        if ori_head==8:
            print("ori_head==8에서 디버깅")
            debug()

        return ori_head
    
def push_head(num, li):
    if num==-1:
        return
    else:
        if num_gift[li]==0:
            head[li]=num
            tail[li]=num
            num_gift[li]+=1
        else:
            ori_head=head[li]
            head[li]=num
            nxt[num]=ori_head
            prv[ori_head]=num
            num_gift[li]+=1

def exchange_front_300(cmd):
    m_src, m_dst = cmd[0], cmd[1]

    src_res = pop_head(m_src)
    dst_res = pop_head(m_dst)
    push_head(src_res, m_dst)
    push_head(dst_res, m_src)
    print(num_gift[m_dst])
    #debug()

def split_400(cmd):
    m_src, m_dst = cmd[0], cmd[1]

    to_move = []
    for _ in range(num_gift[m_src]//2):
        to_move.append(pop_head(m_src))
    to_move.reverse()
    #print(to_move)
    for i in to_move:
        push_head(i, m_dst)
    print(num_gift[m_dst])


def getPresentInfo_500(p_num):
    #for i in getIdx(p_num)
    p_num=p_num[0]
    a = prv[p_num] if prv[p_num] !=0 else -1
    b = nxt[p_num] if nxt[p_num] !=0 else -1

    print(a+2*b)
            
def getBeltInfo_600(b_num):
    b_num=int(b_num[0])
    a = head[b_num] 
    b = tail[b_num]
    if a==-1: a=-1
    if b==-1: b=-1
    c = num_gift[b_num]
    
    print(a+2*b+3*c)

q = int(input())
cmd = list(map(int, input().split()))
factory = build_100(cmd[1:])

for i in range(q-1):
    cmd = list(map(int, input().split()))
    
    if cmd[0] == 200: moveall_200(cmd[1:]); debug()
    if cmd[0] == 300: exchange_front_300(cmd[1:]); debug()
    if cmd[0] == 400: split_400(cmd[1:]); debug()
    if cmd[0] == 500: getPresentInfo_500(cmd[1:]); debug()
    if cmd[0] == 600: getBeltInfo_600(cmd[1:]); debug()

