#include <bits/stdc++.h>
using namespace std;

int t;
int dic[28];

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> t;

    while(t--) {
        string s;
        cin >> s;

        dic[s[0] - 'a']++;
    }

    int cnt = 0;
    for(int i=0; i<27; i++) {
        if(dic[i] >= 5) {
            cout << char('a' + i);
            cnt++;
        }
    }

    if(cnt == 0) {
        cout << "PREDAJA";
    }
    
    return 0;
}