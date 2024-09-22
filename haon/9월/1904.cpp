// n=1 -> 1 (1)
// n=2 -> 2 (00, 11)
// n=3 -> 3 (111, 100, 001)
// n=4 -> 5 (0011, 0000, 1001, 1100, 1111)
#include <bits/stdc++.h>
using namespace std;

int n;
long long arr[1000002];

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n;
    arr[0] = 0; arr[1] = 1; arr[2] = 2;

    for(int i=3; i<=n; i++) {
        arr[i] = (arr[i-1] + arr[i-2]) % 15746;
    }
    cout << arr[n] % 15746;

    return 0;
}