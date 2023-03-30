"""
5 5 5 2
0 0 0 5 2 
0 4 0 0 0 
1 0 4 0 0 
-1 0 3 0 0 
0 0 0 3 0
res: 85
"""
import sys; sys.stdin = open("input.txt", "r")

ddr=[-1,-1,1,1]
ddc=[-1,1,-1,1]
dr=[-1,1,0,0]
dc=[0,0,-1,1]
INF = 99

n, m, k, C = map(int, input().split())
tree=[]
tc = [[0 for i in range(n)] for j in range(n)] #tree candidate
init_tc=tc #tc init
for _ in range(n):
  _tree = list(map(int, input().split()))
  for i in range(n):
    if _tree[i] == -1: _tree[i] = -INF #벽을 -INF로
  tree.append(_tree)
  


def debug():
  return
  print("***debug***")
  print(f"격자크기 n= {n}")
  print(f"박멸 진행년수 m= {m}")
  print(f"제초제 확산범위 k={k}")
  print(f"제초제 남아있는 년수 기본 c={C}")
  print("tree map")
  for i in tree:
    print(i)
  print()

def tc_debug():
  for _ in tc:
    print(_)
#################### 1. 성장 ########################
def getAdjTrees(r,c):
  adj = 0
  for i in range(4):
    nr, nc = r+dr[i], c+dc[i]
    if 0<=nr<n and 0<=nc<n and tree[nr][nc]>0:
      adj += 1
  return adj

def growth():
  for r in range(n):
    for c in range(n):
      if tree[r][c]>0:
        tree[r][c] += getAdjTrees(r,c)
#################### 2. 번식 ########################
#def set
def adjTreeSpread(r, c, tn):
  adj, bn = 0, 0
  #사방으로 빈칸 찾기
  for i in range(4):
    nr, nc = r+dr[i], c+dc[i]
    if 0<=nr<n and 0<=nc<n and tree[nr][nc]==0: #tree[r][c]가 양수 -> 나무가 있음, 음수면 제초제있는곳 또는 벽, 0이면 빈칸으로 뻗어나갈 수 있음
      bn += 1

  #빈칸에 treenum//bn만큼 트리 추가하기
  for i in range(4):
    nr, nc = r+dr[i], c+dc[i]
    if 0<=nr<n and 0<=nc<n and tree[nr][nc]==0:
      tc[nr][nc] += tn//bn


      
  
def treeSpread():
  global tc
  for r in range(n):
    for c in range(n):
      if tree[r][c]>0: 
        adjTreeSpread(r, c, tree[r][c])
  
  for r in range(n):
    for c in range(n):
      tree[r][c] += tc[r][c]

  tc=[[0 for i in range(n)] for j in range(n)] #tree candidate   
  
#################### 3. 제초제 선택 ########################
anti = [[0 for i in range(n)] for j in range(n)] #anti candidate
init_anti=anti


def getDiagVal(r,c):
  anti[r][c]+=tree[r][c]
  nogo = [False]*4

  for i in range(4):
    for reach in range(1,k+1): #k번 만큼
      if nogo[i]: continue #한 번 벽이나 빈칸 맞았으면 그쪽 방향으로 더 진행 안함
      nr, nc = r+ddr[i]*reach, c+ddc[i]*reach

      if 0<=nr<n and 0<=nc<n and tree[nr][nc]>0: #범위 벗어나면 continue
        anti[r][c] += tree[nr][nc]
      else:
        nogo[i] = True
        continue


def selectAnti():
  global anti
  mr, mc = -1, -1
  #사방으로 나무 찾기
  for r in range(n):
    for c in range(n):
      if tree[r][c]>0: 
        getDiagVal(r,c)
  

  mr, mc, mval = -1,-1,-1
  for r in range(n):
    for c in range(n):
      if anti[r][c] > mval:
        mr, mc, mval = r, c, anti[r][c]
  
  anti = [[0 for i in range(n)] for j in range(n)] 
  return mr, mc, mval

  
#################### 4. 제초제 뿌리기 ########################
#지정한 위치에서 가능한 방향대로 제초제를 뿌리기
#빈칸인 경우 그 칸만 제초제가 닿고 그 이상으로 뻗지 않음
#벽도 제초제로 리셋되는 것으로 가정

def spreadAnti(r, c):
  tree[r][c] = -C
  nogo = [False]*4
  for i in range(4):
    for reach in range(1,k+1): #k번 만큼

      if nogo[i]:

        continue #한 번 벽이나 빈칸 맞았으면 그쪽 방향으로 더 진행 안함
      
      nr, nc = r+ddr[i]*reach, c+ddc[i]*reach

      if nr<0 or nr>=n or nc<0 or nc>=n: #범위 벗어나면 nogo True & continue
        nogo[i] = True
        continue
      if tree[nr][nc]>0: # 나무 있으면
        tree[nr][nc] = -C #c년동안 제초제 작동
      elif tree[nr][nc]==0: #빈칸이면
        tree[nr][nc] = -C #c년동안 제초제 작동
        nogo[i] = True #그리고 더이상 진행안함
        continue
      elif tree[nr][nc]<0 : #이미 제초제가 있으면(벽 포함됨)
        if tree[nr][nc]==-INF: 
          nogo[i]=True
          continue #벽이면 pass

        tree[nr][nc] = -C #제초제 c년으로 리셋
        nogo[i] = True
  
def meltAnti(): # 한 해가 지나서 제초제들 1년씩 녹슬었음
  for r in range(n):
    for c in range(n):
      v=tree[r][c]
      if v<0 and v!=-INF:
        tree[r][c] += 1

ans = 0
for _ in range(m):
  growth()
  treeSpread()
  mr, mc, _ans = selectAnti()
  ans += _ans
  meltAnti() 
  spreadAnti(mr, mc)
print(ans)
