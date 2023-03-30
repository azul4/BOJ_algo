import sys;

sys.stdin = open("input.txt", "r")
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

def debug(a):
    print("arr print:")
    for i in a: print(i)

ans = -1

def getMax(arr):
    global ans
    for li in arr:
        if ans < max(li):
            ans = max(li)


def leftpush(parr):
    temp = [0] * (n + 1)
    # 왼쪽으로 쏠리기
    idx = 0
    for j in range(n):
        if parr[j] == 0: continue
        temp[idx] = parr[j]
        idx += 1
    # 더할거 더하기
    for j in range(n):
        cur = temp[j]
        nxt = temp[j + 1]
        if cur == nxt:
            temp[j] *= 2
            temp[j + 1] = 0
    # 다시 왼쪽으로 밀기
    retli = [0] * n
    lidx = 0
    for ni in range(n):
        if temp[ni] != 0:
            retli[lidx] = temp[ni]
            lidx += 1
    return retli


def rightpush(parr):
    # 오른쪽으로 쏠리기
    temp = [0] * (n + 1)
    idx = n - 1
    for j in range(n - 1, -1, -1):
        if parr[j] == 0: continue
        temp[idx] = parr[j]
        idx -= 1

    # 더할거 더하기
    for j in range(n - 1, -1, -1):
        cur = temp[j]
        nxt = temp[j - 1]
        if cur == nxt:
            temp[j] *= 2
            temp[j - 1] = 0

    # 다시 왼쪽으로 밀기
    lidx = n - 1
    retli = [0] * n
    for ni in range(n - 1, -1, -1):
        if temp[ni] != 0:
            retli[lidx] = temp[ni]
            lidx -= 1
    return retli


def up(arr, t):
    if t == 5:
        getMax(arr)
        return
    for r in range(n):
        to_list = []
        for c in range(n):
            to_list.append(arr[c][r])
        to_list = leftpush(to_list)
        for c in range(n):
            arr[c][r] = to_list[c]

    oarr = arr[:][:]
    up(arr, t+1);
    arr = oarr[:][:]
    down(arr, t+1);
    arr = oarr[:][:]
    left(arr, t+1);
    arr = oarr[:][:]
    right(arr, t+1);
    arr = oarr[:][:]



def down(arr, t):
    if t == 5:
        getMax(arr)
        return

    for r in range(n):
        to_list = []
        for c in range(n):
            to_list.append(arr[c][r])
        to_list = rightpush(to_list)
        for c in range(n):
            arr[c][r] = to_list[c]



    oarr = arr[:][:]
    up(arr, t+1);
    arr = oarr[:][:]
    down(arr, t+1);
    arr = oarr[:][:]
    left(arr, t+1);
    arr = oarr[:][:]
    right(arr, t+1);


def left(arr, t):
    if t == 5:
        getMax(arr)
        return
    for i in range(n):
        arr[i] = leftpush(arr[i])

    oarr = arr[:][:]
    up(arr, t+1);
    arr = oarr[:][:]
    down(arr, t+1);
    arr = oarr[:][:]
    left(arr, t+1);
    arr = oarr[:][:]
    right(arr, t+1);



def right(arr, t):
    if t == 5:
        getMax(arr)
        return
    for i in range(n):
        arr[i] = leftpush(arr[i])

    oarr = arr[:][:]
    up(arr, t+1);
    arr = oarr[:][:]
    down(arr, t+1);
    arr = oarr[:][:]
    left(arr, t+1);
    arr = oarr[:][:]
    right(arr, t+1);



def simul(arr):
    oarr = arr[:][:]
    up(arr, 1); #debug(arr);
    arr = oarr[:][:]
    down(arr, 1);#debug(arr);
    arr = oarr[:][:]
    left(arr, 1);#debug(arr);
    arr = oarr[:][:]
    right(arr, 1);#debug(arr);


simul(arr)
print(ans)
