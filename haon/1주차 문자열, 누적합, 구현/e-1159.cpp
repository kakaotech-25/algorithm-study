#include <bits/stdc++.h>
using namespace std;

int n;
int alpha[26];
string s = "abcdefghijklmnopqrstuvwxyz";

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n;
    for(int i=0; i<n; i++) {
        string input;
        cin >> input;
        alpha[input[0] - 'a']++;
    }

    bool predaja = true;
    for(int i=0; i<26; i++) {
        if(alpha[i] >= 5) {
            cout << s[i];
            predaja = false;
        }
    }

    if(predaja) {
        cout << "PREDAJA";
    }

    return 0;
}