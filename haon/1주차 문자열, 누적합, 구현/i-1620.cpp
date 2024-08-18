#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<string> res;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> m;

    unordered_map<string, int> dic1;
    unordered_map<int, string> dic2;

    for(int i=1; i<=n; i++) {
        string s;
        cin >> s;
        dic1[s] = i;
        dic2[i] = s;
    }    

    while(m--) {
        string s;
        cin >> s;

        if(s[0] > '0' && s[0] <= '9') {
            cout << dic2[stoi(s)] << "\n";
        } else {
            cout << dic1[s] << "\n";
        }
    }

    return 0;
}