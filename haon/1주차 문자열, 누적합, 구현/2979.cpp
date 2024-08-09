#include <bits/stdc++.h>
using namespace std;

int a, b, c;
int cnt[102];

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> a >> b >> c;
    b = b*2;
    c = c*3;

    for(int i=0; i<3; i++) {
        int start, end;
        cin >> start >> end;

        for(int j=start; j<end; j++) {
            cnt[j]++;
        }
    }

    int res = 0;
    for(int i=1; i<=100; i++) {
        if(cnt[i] == 1) {
            res += a;
        } else if(cnt[i] == 2) {
            res += b;
        } else if(cnt[i] == 3) {
            res += c;
        }
    }
    cout << res;

    return 0;
}