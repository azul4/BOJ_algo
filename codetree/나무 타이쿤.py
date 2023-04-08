import sys; sys.stdin=open("input.txt", "r")
dr=[0,-1,-1,-1,0,1,1,1]
dc=[1,1,0,-1,-1,-1,0,1]

def moveNMap(omap, d, p): #old map
    nmap = [[0 for _ in range(n)] for _ in range(n)] #new nutri map
    for r in range(n):
        for c in range(n):
            if omap[r][c]:
                nr, nc = (r+dr[d]*p)%n, (c+dc[d]*p)%n
                nmap[nr][nc] = omap[r][c]
    return nmap

def injectNutri(tmap, nmap):
    for r in range(n):
        for c in range(n):
            if nmap[r][c]:
                #2. 영양제 땅 높이 1 증가
                tmap[r][c] += 1
    return tmap

def growthDiagTree(tmap, nutri):
    # 3. 영양제 대각선 땅에 나무 있으면 +1
    ddr = [-1,-1,1,1]
    ddc = [1,-1,1,-1]
    for r in range(n):
        for c in range(n):
            if nutri[r][c]:
                diag = []
                for _ in range(4): diag.append([r + ddr[_], c + ddc[_]])
                for can in diag:
                    nr, nc = can[0], can[1]
                    if 0 <= nr < n and 0 <= nc < n and tmap[nr][nc]:
                        tmap[r][c] += 1
    return tmap

def cutTree(tmap, nmap):
    nnmap = [[0 for _ in range(n)] for _ in range(n)]

    for r in range(n):
        for c in range(n):
            if nmap[r][c]: continue
            if tmap[r][c] >= 2:
                tmap[r][c] -= 2
                nnmap[r][c] = 1

    return tmap, nnmap
#main
n, m = map(int, input().split())
tree = [list(map(int, input().split())) for _ in range(n)]
rule = [list(map(int, input().split())) for _ in range(m)]
nutri = [[0 for i in range(n)] for i in range(n)]
nutri[-1][0] = nutri[-1][1] = nutri[-2][0] = nutri[-2][1] = 1
ans = 0

for i in range(m):
    #1. move
    d, p = rule[i]
    nutri = moveNMap(nutri, d-1, p)
    #2. inject nutri
    tree = injectNutri(tree, nutri)
    #3. grow tree
    tree = growthDiagTree(tree, nutri)
    #4. cut 2
    tree, nutri = cutTree(tree, nutri)

    #합계 구하기
for r in range(n):
    ans += sum(tree[r])
print(ans)