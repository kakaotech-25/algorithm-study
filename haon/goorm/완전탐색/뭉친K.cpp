#include <bits/stdc++.h>
using namespace std;

int k;
int num[15];
bool isused[3000002];
int sum;
int ans;

void func(int n, int total) {
    if(total >= 1) {
        if(!isused[total]) {
            ans++;
        }
        isused[total] = true;
    }

    if(n == k) {
        return;
    }

    func(n+1, total + num[n]);
    func(n+1, total - num[n]);
    func(n+1, total);
}

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> k;
    for(int i=0; i<k; i++) {
        cin >> num[i];
        sum += num[i];
    }

    func(0, 0);

    cout << sum - ans;

    return 0;
}