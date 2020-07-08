#include <iostream>
#pragma warning(disable:4996)
using namespace std;

int main()
{
	int input;
	int ref[41] = { 0, 1 };
	for (int i = 2; i < sizeof(ref) / sizeof(ref[0]); i++)
	{
		ref[i] = ref[i - 1] + ref[i - 2];
	}
	scanf("%d", &input);

	for (int i = 0; i < input; i++)
	{
		int temp;
		scanf("%d", &temp);
		if (temp == 0)
			printf("1 0\n");
		else
			printf("%d %d\n", ref[temp-1], ref[temp]);
	}
}

/************
* 재귀함수 형태로는 시간초과.
* 0과 1의 규칙을 찾아서 미리 ref 배열에 값을 저장.
* 후에 단순 print
************/
