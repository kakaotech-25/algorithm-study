#include <bits/stdc++.h>
using namespace std;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    bool isPalin = true;
    string s;
    cin >> s;
    int len = s.length();

    for(int i = 0; i < len; i++){
        for(int j=len-1; j>=i; j--){
            if(s[i] != s[j]){
                isPalin = false;
            }
        }
    }

    if(isPalin) {
        cout << 1;
    } else {
        cout << 0;
    }

    return 0;
}