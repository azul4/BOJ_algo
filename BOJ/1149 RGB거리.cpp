/*
* 0611 일지
* 최솟값이 뭔가 잘못 불러지는중
* minimum + next()가 아닌가?
*/


#include <iostream>
#include <algorithm>
#define R 0
#define G 1
#define B 2
using namespace std;
int dp(int** ary, const int n);
int next(int** ary, int from, int i, const int n);

int main()
{
	int n;
	cin >> n;
	int** ary = new int*[n];
	for (int i = 0; i < n; i++) ary[i] = new int[3];

	for (int i = 0; i < n; i++)
	{
		cin >> ary[i][0] >> ary[i][1] >> ary[i][2];
	}
	cout << dp(ary, n);
}

int dp(int** ary, const int n)
{
	int start_R = ary[0][R] + next(ary, R, 0, n);
	int start_G = ary[0][G] + next(ary, G, 0, n);
	int start_B = ary[0][B] + next(ary, B, 0, n);
	return min({ start_R, start_G, start_B });
}

int next(int** ary, int from, int i, const int n)
{
	int row = i + 1;
	if (row == n)
	{
		if (from == R) return min(ary[i][G], ary[i][B]);
		if (from == G) return min(ary[i][R], ary[i][B]);
		if (from == B) return min(ary[i][R], ary[i][G]);
	}
	else
	{
		int minimum;
		if (from == R)
			minimum = min(next(ary, G, row, n), next(ary, B, row, n));

		else if (from == G)
			minimum = min(next(ary, R, row, n), next(ary, B, row, n));

		else if (from == B)
			minimum = min(next(ary, R, row, n), next(ary, G, row, n));

		else
			throw "neither R, G, nor B";
		return minimum + ary[i][from];
	}
}