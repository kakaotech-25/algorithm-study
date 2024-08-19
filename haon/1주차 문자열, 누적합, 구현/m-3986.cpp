#include <bits/stdc++.h>
using namespace std;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int ans = 0;
    int t;
    cin >> t;
    while(t--) {
        stack<char> st;
        string s;
        cin >> s;

        for(int i=0; i<s.size(); i++) {
            if(st.empty() || st.top() != s[i]) {
                st.push(s[i]);
            }
            else if(st.top() == s[i]) {
                st.pop();
            }
        }

        if(st.empty()) {
            ans++;
        }
    }
    cout << ans;

    return 0;
}