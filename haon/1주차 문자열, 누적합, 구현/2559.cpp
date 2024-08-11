#include <bits/stdc++.h>
using namespace std;

int n, m;
unordered_map<string, int> dic1;
unordered_map<int, string> dic2;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> m;

    for(int i=1; i<=n; i++) {
        string s;
        cin >> s;
        dic1[s] = i;
        dic2[i] = s;
    }
    

    while(m--) {
        string input;
        cin >> input;

        if(input[0] - '0' >= 0 && input[0] <= 9) {
            cout << dic2[stoi(input)] << "\n";
        } else {
            cout << dic1[input] << "\n";
        }
    }

    return 0;
}