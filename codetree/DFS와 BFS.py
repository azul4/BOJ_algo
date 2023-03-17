n, m, f = map(int, input().split())
line = []
arr = [[0 for i in range(n+1)] for i in range(n+1)]
for i in range(m):
    s,e = map(int, input().split())
    arr[s][e] = arr[e][s] = 1

dfs_visited = [False]*(n+1)
dfs_order = []
def dfs(f):
    global dfs_visited
    dfs_order.append(f)
    dfs_visited[f]=True
    for i in range(1,n+1):
        if not dfs_visited[i] and arr[f][i]:
            dfs(i)
            
bfs_order=[]
def bfs(f):
    from collections import deque
    visited = [False]*(n+1)
    order = []

    q = deque()
    visited[f]=True
    q.append(f)
    bfs_order.append(f)

    while q:
        node = q.popleft()

        for i in range(1, n+1):
            if visited[i]:
                continue
            if arr[node][i]:
                visited[i]=True
                q.append(i)
                bfs_order.append(i)
    
    #끝나면 순회한 대로 프린트


dfs(f)
#출력부분
for i in dfs_order:
    print(i, end=' ')
print()
bfs(f)
for i in bfs_order:
    print(i, end=' ')
print()