T = int(input())

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

dr = [-1,0,1,0]
dc = [0,1,0,-1]
blk = [list()] * 11
blk[1] = [2, 3, 1, 0]
blk[2] = [1, 3, 0, 2]
blk[3] = [3, 2, 0, 1]
blk[4] = [2, 0, 3, 1]
blk[5] = [2, 3, 0, 1]  # 사각형


def simul(sr, sc, _dir):
    score = 0
    r, c, dir = sr, sc, _dir
    while True:
        #이미 위치한 곳에 삼/사각형 있으면 방향부터 바꾸고 시작
        nr, nc = r+dr[dir], c+dc[dir]
        #삼각형 사각형 만나면 방향 바꿈 - 벽 포함
        if 1 <= MAP[nr][nc] <= 5:
            tri = MAP[nr][nc]
            dir = blk[tri][dir]
            score += 1

        #웜홀 만나면 위치 바꿈
        elif 6 <= MAP[nr][nc] <= 10:
            hidx = MAP[nr][nc]
            nr, nc = blk[hidx][0] if [nr,nc] == blk[hidx][1] else blk[hidx][1]

        #블랙홀 만나면 게임 끝
        elif MAP[nr][nc] == -1:
            return score

        #처음 위치면 게임종료
        elif (nr, nc) == (sr, sc):
            return score
        r, c = nr, nc



# main
for tc in range(1,T+1):
    #init
    n = int(input())
    wall = [5] * (n + 2)
    MAP = list()
    MAP.append(wall)
    for _ in range(n):
        MAP.append([5] + list(map(int, input().split())) + [5])
    MAP.append(wall)

    for ii in range(6,11):
        blk[ii] = list()
    for i in range(1,n+1):
        for j in range(1,n+1):
            if MAP[i][j] == -1:  # 블랙홀
                blk[0] = [i, j]
                continue

            if 6 <= MAP[i][j] <= 10:  # 웜홀
                idx = MAP[i][j]
                if len(blk[idx]) == 0:
                    blk[idx] = [[i,j]]
                else:
                    blk[idx].append([i,j])

    #sol
    s = [0]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if MAP[i][j] == 0:
                for _d in range(4):
                    res = simul(i, j, _d)
                    if res: s.append(res)

    print(f"#{tc} {max(s)}")
