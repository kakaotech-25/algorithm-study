#include <bits/stdc++.h>
using namespace std;

int n, k;
int sum[100002];

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> k;

    for(int i=1; i<=n; i++) {
        int data;
        cin >> data;
        sum[i] = sum[i-1] + data;
    }

    int ans = -2100000000;
    for(int i=k; i<=n; i++) {
        ans = max(ans, sum[i] - sum[i-k]);
    }
    cout << ans;

    return 0;
}