def memoization(fuel):
    memo[1] = [[fuel[1], 0]]
    for i in range(2, fuel[0]):
        prv = memo[i - 1]
        for j in range(len(prv)):
            pow, cng = prv[j][0], prv[j][1]
            can1, can2 = [pow-1, cng], [fuel[i], cng+1]
            if can1[0] > 0:
                memo[i].append(can1)
            if can2[0] >= pow:
                memo[i].append(can2)

    return min([memo[i][k][1] for k in range(len(memo[i]))])

# main
T = int(input())
for tc in range(T):
    memo = [[] for i in range(1000)]
    fuel = list(map(int, input().split()))
    print(f"#{tc + 1} {memoization(fuel)}")
