N = int(input())
dots = [[0,0]]
visited = [False] * (N+1)

for _ in range(N):
    li = list(map(int, input().split()))
    dots.append(li)

def possible(s, e):
    if s==e:
        return False
    if visited[e]: 
        return False
    #진출하려는 노드 사이에 다른 정점이 존재하지 않으면 바로 true
    midnode = []
    sdot, edot = dots[s], dots[e]
    for i in range(1, N+1):
        mdot = dots[i]
        if i==s or i==e: continue
        if not visited[i]:            return True

        #if sdot[0] == edot[0] and edot[0] == mdot[0]:
        #    if sdot[1] < mdot[1] < edot[1] or sdot[1] > mdot[1] > edot[1]:
        #        return True
        #if sdot[1] == edot[1] and edot[1] == mdot[1]:
        #    if sdot[0] < mdot[0] < edot[0] or sdot[0] > mdot[0] > edot[0]:
        #        return True 
        if sdot[0] != edot[0] or edot[0] != mdot[0] or mdot[0] != sdot[0]: return True
        if sdot[1] != edot[1] or edot[1] != mdot[1] or mdot[1] != sdot[1]: return True
        #print("{}와 {} 경로상에 정점 {}가 존재함.".format(s, e, i))
        #정점이 존재하지만 방문하지 않았을 경우 true
        #둘다 아니면 false
        return False

cnt = 0
def bt(node, trial):
    global cnt
    #print(f"got into {node}")
    if trial==N:
        cnt += 1
        return

    visited[node] = True
    for i in range(1, N+1): # 1~idx까지 순회됨
        if possible(node, i): 
            #print(f"going {i}")
            bt(i, trial+1)
    visited[node]=False

bt(0, 0)
print(cnt)