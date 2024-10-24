#include <bits/stdc++.h>
using namespace std;

int cnt;
int num[22];
int n, s;

void func(int k, int total) {
    if(k == n) {
        if(total == s) {
            cnt++;
        }
        return;
    }

    func(k+1, total);
    func(k+1, total + num[k]);
}

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> s;

    for(int i=0; i<n; i++) {
        cin >> num[i];
    }

    func(0, 0);

    // 아무것도 선택하지 않은 경우 (공집한인 경우) 를 제거
    if(s == 0) {
        cnt--;
    }

    cout << cnt;

    return 0;
}