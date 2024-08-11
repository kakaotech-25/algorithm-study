#include <bits/stdc++.h>
using namespace std;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    string s;
    getline(cin, s);

    for(int i = 0; i < s.size(); i++) {
        char c = s[i];
        if ('a' <= c && c <= 'z') {
            // 소문자인 경우
            c = (c - 'a' + 13) % 26 + 'a';
        } else if ('A' <= c && c <= 'Z') {
            // 대문자인 경우
            c = (c - 'A' + 13) % 26 + 'A';
        }
        cout << c;
    }

    return 0;
}
