import sys; sys.stdin = open("input.txt", "r")

n = int(input())
order = [list(map(int, input().split())) for _ in range(8)]
block = [list(map(int, input().split())) for _ in range(n)]
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,-1,-1,-1,0,1,1,1]
MAP = [[0]*4 for i in range(101)]
score = 0
map_loc = list() #박스의 현재 [r,c]
idx = [-1]*4

def setBlock(b):
    r = idx[b[1] - 1]
    c = b[1]-1
    map_loc.append([r,c,b[0]])

def moveMap(i):
    for ii in range(len(map_loc)):
        val = map_loc[ii][2]
        for j in range(8):
            nr = map_loc[ii][0] + dr[order[val-1][j]-1] #위로 올라가는 방향이라 빼기가 맞음
            nc = map_loc[ii][1] + dc[order[val-1][j]-1]
            if not (-101<=nr<=-1) or not (0<=nc<=3):
                continue
            map_loc[ii] = [nr,nc,val]
            break


def removeBlock():
    global score
    for r in range(-1, -101, -1):
        if min(MAP[r]) == 0:
            return
        score += 1
        MAP[r] = [0,0,0,0]

def dropBlock():
    global map_loc, idx
    nl = [list(), list(), list(), list()]
    for ii in range(len(map_loc)):
        nl[map_loc[ii][1]].append(map_loc[ii][0])

    map_loc = list()
    for r in range(4):
        c = -1
        for val in nl[r]:
            map_loc.append([c, r, val])
            r -= 1

    #drop 끝나고 다음 박스를 위한 idx 세팅
    idx = [-1]*4
    for elem in map_loc:
        idx[elem[1]] -= 1

def countLine():
    return abs(max(idx)) - 1

def delLine(line):
    global map_loc
    new_map_loc = list()
    for i in range(len(map_loc)):
        if not (-line <= map_loc[i][0] <= 1):
            r, c, val = map_loc[i][0] + line, map_loc[i][1], map_loc[i][2]
            if r > 0:
                new_map_loc.append(map)
    map_loc = new_map_loc

def simul(b):
    tot_line = 0
    setBlock(b)
    #print(f"{b} in simul1")
    moveMap(i)
    dropBlock()
    while True:
        line = countLine()
        if not line: break
        tot_line += line
        delLine(line)
        dropBlock()
        moveMap(i)
    return tot_line


def simul2(i):
    b = block[i]
    score_list = [0,0,0,0,0]
    for ii in range(i, len(block)):
        #print(f"{ii}에서 simul2 준비")
        for j in range(1, 5):
            block[i][1] = j
            #print(f"{b} in simul2-------------ii={ii}")
            score_list[j] = simul(b)
            #print(f"score_list={score_list}")
            # 다음 것도 골라야하는 상황이 온다면
            # 재귀를 돌려야 함
            if ii+1 < len(block) and block[ii+1][1]==0:
                #print(f"call simul2 with param {ii+1}")
                score_list[j] += simul2(ii+1)
            block[i][1] = 0

    return max(score_list[1:5])

for i in range(len(block)):
    b = block[i]
    if b[1] != 0:
        score += simul(b)
    else:
        #print(f"call simul2 with param {i}")
        score += simul2(i)

print(score)

#골3 이라고는 하는데... 플레같은 난이도이다 ㅠㅠ