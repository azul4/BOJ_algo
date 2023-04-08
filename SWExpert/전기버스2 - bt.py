import sys; sys.stdin=open("input.txt", "r")
ans = 999
change = 0
changed = False
c=[]
def bt(t, fuel, pow):
    global change, ans, changed

    if changed and change >= ans:
        return
    if pow == 0:
        return
    if t==fuel[0] and pow >= 0:
        ans = min(change, ans)
        changed = True
        return
    pow -= 1
    #change
    change += 1
    c.append(t)
    bt(t+1, fuel, fuel[t])
    change -= 1
    c.pop()

    #don't change
    bt(t+1, fuel, pow)

#main
T = int(input())
for tc in range(T):
    fuel = list(map(int, input().split()))
    bt(2, fuel, fuel[1])
    print(f"#{tc+1} {ans}")
    ans = 999
    change = 0
    changed = False
