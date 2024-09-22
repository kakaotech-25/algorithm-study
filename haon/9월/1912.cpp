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