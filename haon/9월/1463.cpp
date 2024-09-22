#include <bits/stdc++.h>
using namespace std;

int n;
int arr[1000001]; // arr[i] : 정수 i을 1로 만드는데 필요한 최소 연산수

int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  cin >> n;

  arr[1] = 0;
  // arr[i] = min(arr[i/3], arr[i/2], arr[i-1]) + 1;

  for(int i=2; i<=n; i++) {
    arr[i] = arr[i-1] + 1;
    if(i % 2 == 0) {
      arr[i] = min(arr[i], arr[i/2] + 1);
    }
    if(i % 3 == 0) {
      arr[i] = min(arr[i], arr[i/3] + 1);
    }
  }
  cout << arr[n];

  return 0;
}