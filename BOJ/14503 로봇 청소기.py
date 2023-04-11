#import sys; sys.stdin = open("input.txt", "r")

dr = [-1,0,1,0]
dc = [0,1,0,-1] # 북 동 남 서, 위 오른 아래 왼
n, m= map(int, input().split())
r, c, d = map(int, input().split())
MAP = [list(map(int, input().split())) for i in range(n)]
nr, nc = 0, 0
cnt = 0
while True:
#for _ in range(50):
    #1. 청소하기
    if MAP[r][c]==0:
        MAP[r][c] = 2
        cnt += 1
    nr = [r+dr[0], r+dr[1], r+dr[2], r+dr[3]]
    nc = [c+dc[0], c+dc[1], c+dc[2], c+dc[3]]
    # 4방향중 청소되지 않은 빈 칸이 있는 경우
    if MAP[nr[0]][nc[0]]==0 or MAP[nr[1]][nc[1]]==0 \
        or MAP[nr[2]][nc[2]]==0 or MAP[nr[3]][nc[3]]==0:
        d = (d+3)%4
        if MAP[r+dr[d]][c+dc[d]] == 0:
            r, c = r + dr[d], c + dc[d]
            continue
    # 4방향중 청소되지 않은 빈 칸이 없는 경우
    else:
        td = (d+2)%4
        tr, tc = r+dr[td], c+dc[td]
        if MAP[tr][tc] == 1:
            break
        elif MAP[tr][tc] == 0 or MAP[tr][tc]==2:
            r, c = tr, tc
            continue


print(cnt)
