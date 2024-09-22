#include <bits/stdc++.h>
using namespace std;

int t;
long long arr[102];

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> t;

    arr[1] = arr[2] = arr[3] = 1;

    for(int i=4; i<=100; i++) {
        arr[i] = arr[i-2] + arr[i-3];
    }

    while(t--) {
        int n;
        cin >> n;
        cout << arr[n] << "\n";       
    }

    return 0;
}