#include <bits/stdc++.h>
using namespace std;

int n;
int arr[1002][4];
int d[1002][4]; // d[i][j] : i번째 집을 색깔 j로 칠하는데 소모한 최소 비용
// j=1 => 빨강 / j=2 => 초록 / j=3 => 파랑
// d[i][1] = min(d[i-1][2], d[i-1][3]) + arr[i][1];
// d[i][2] = min(d[i-1][1], d[i-1][3]) + arr[i][2];
// d[i][3] = min(d[i-1][1], d[i-1][2]) + arr[i][3];

int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  cin >> n;

  for(int i=0; i<n; i++) {
    int r, g, b;
    cin >> r >> g >> b;

    arr[i][1] = r;
    arr[i][2] = g;
    arr[i][3] = b;    
  }

  for(int i=0; i<n; i++) {
    d[i][1] = min(d[i-1][2], d[i-1][3]) + arr[i][1];
    d[i][2] = min(d[i-1][1], d[i-1][3]) + arr[i][2];
    d[i][3] = min(d[i-1][1], d[i-1][2]) + arr[i][3];
  }

  int minValue = d[n-1][1];
  minValue = min(minValue, d[n-1][2]);
  minValue = min(minValue, d[n-1][3]);

  cout << minValue;

  return 0;
}