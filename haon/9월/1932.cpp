#include <bits/stdc++.h>
using namespace std;

int arr[502][502];
int d[502][502];

int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  int n;
  cin >> n;
  for(int i=1; i<=n; i++) {
    for(int j=1; j<=i; j++) {
      cin >> arr[i][j];
    }
  }

  d[1][1] = arr[1][1];

  for(int i=2; i<=n; i++) {
    for(int j=1; j<=i; j++) {
      d[i][j] = max(d[i-1][j-1], d[i-1][j]) + arr[i][j];
    }
  }

  cout << *max_element(d[n] + 1, d[n] + n + 1);

  return 0;
}