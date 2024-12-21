#include <bits/stdc++.h>
using namespace std;

int n;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n;

    long long mx = 0;
    for(int num=1; num<=n; num++) {
        long long cur = num;
        long long res = 1;

        while (cur >= 1) {
            res = res * (cur % 10);
            cur /= 10;
        }

        mx = max(mx, res);        
    }

    cout << mx;

    return 0;
}