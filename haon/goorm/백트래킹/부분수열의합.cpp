#include <bits/stdc++.h>
using namespace std;

int n, s;
int ans;
int arr[22];

void func(int k, int total) {
    if(k == n) {
        if(total == s) {
            ans++;
        }
        return;
    }

    func(k+1, total);
    func(k+1, total + arr[k]);
}

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> s;

    for(int i=0; i<n; i++) {
        cin >> arr[i];
    }

    func(0, 0);

    if(s == 0) {
        ans--;
    }

    cout << ans;

    return 0;
}