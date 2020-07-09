#include <stdio.h>
#pragma warning(disable:4996)

int main()
{
	int dp[1001];
	dp[0] = 0;
	dp[1] = 1;
	dp[2] = 2;
	for (int i = 3; i < sizeof(dp)/sizeof(dp[0]); i++)
	{
		dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;
	}

	int n;
	scanf("%d", &n);
	printf("%d", dp[n]);
}
