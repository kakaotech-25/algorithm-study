// n번까지의 연속합의 최대값은 [n-1번까지의 최대값 + n번 값] or [n번 값] 둘 중 큰 값이다.

#include <bits/stdc++.h>
using namespace std;

int arr[100002];
int dp[100002];
int n, res;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n;

    for(int i=0; i<n; i++) {
        cin >> arr[i];
    }
    res = arr[0];
    dp[0] = arr[0];

    for(int i=1; i<n; i++) {
        dp[i] = max(dp[i-1] + arr[i], arr[i]);
        res = max(dp[i], res);
    }
    cout << res;

    return 0;
}