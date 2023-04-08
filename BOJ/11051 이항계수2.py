n, k = map(int, input().split())

memo = [[0]*1010 for _ in range(1010)]
for i in range(1010):
    memo[i][0] = 1
    memo[i][i] = 1

for i in range(2, n+1):
    for j in range(1, i):
        memo[i][j] = (memo[i-1][j-1]%10007 + memo[i-1][j]%10007)%10007

print(memo[n][k])