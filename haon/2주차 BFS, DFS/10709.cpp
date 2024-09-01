#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	ios:: sync_with_stdio(0);
	cin.tie(0);
	int n,m;
	cin >> n >> m;
	vector arr(n,vector<int>(m,0));
	for (int i = 0;i < n;i++)
	{
		string s;
		cin >> s;

		for (int j=0; j < m;j++)
		{
			if (j != 0 && arr[i][j-1] == 0)
				arr[i][j] = 1;
			else if (j == 0  || s[j-1] == '.' && s[j] == '.' && arr[i][j-1] == -1)
				arr[i][j] =  -1;
			else
				arr[i][j] = arr[i][j - 1]+ 1;
			if (s[j]=='c')
				arr[i][j] = 0;
		}
	}
	for (int i=0;i < n; i++)
	{
		for (int j=0;j < m;j++)
		{
			cout << arr[i][j] << ' ';
		}
		cout << "\n";
	}
}