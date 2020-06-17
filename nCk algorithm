#include <iostream>
#include <algorithm>
using namespace std;
int bin(int, int);
int bin2(int, int);
int main()
{
	cout << bin(5, 3) << endl;
	cout << bin(10, 2) << endl;
	cout << bin(6, 3) << endl;
	cout << bin2(5, 3) << endl;
}
int bin(int n, int k)
{
	if (k == 0 || n == k)
		return 1;
	else
		return bin(n - 1, k - 1) + bin(n - 1, k);
}
int bin2(int n, int k)
{
	int i, j;
	int b[100][100];
	for (i = 0; i <= n; i++)
	{
		for (j = 0; j <= min(i, k); j++)
		{
			if (j == 0 || j == i) b[i][j] = 1;
			else b[i][j] = b[i - 1][j - 1] + b[i - 1][j];
		}
	}
	return b[n][k];
}

//bin, bin2 모두 (n, k) 즉 nCk 구하는 알고리즘
