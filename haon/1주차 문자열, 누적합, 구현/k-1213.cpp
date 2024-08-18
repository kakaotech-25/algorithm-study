#include <bits/stdc++.h>
using namespace std;

string s, ans;
int alpha[26];

bool canNotMakePlain() {
    int cnt = 0;
    for(int i=0; i<26; i++) {
        if(alpha[i] % 2 == 1) {
            cnt++;
        }
    }
    return cnt > 1;
}

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> s;
    for(int i=0; i<s.size(); i++) {
        alpha[s[i] - 'A']++;
    }

    if(canNotMakePlain()) {
        cout << "I'm Sorry Hansoo"; 
        return 0;
    }

    // . 'A'부터 'Z'까지 나온 알파벳의 개수/2만큼 알파벳을 정답변수 ans에 더해준다.
    for(int i=0; i<26; i++) {
        for(int j=0; j<alpha[i]/2; j++) {
            ans += i + 'A';
        }
    }

    // 남은 홀수개의 알파벳 1개는 팰린드롬을 만들려면 중앙에 위치해야 하므로 그 후에 더해준다.
    for(int i=0; i<26; i++) {
        if(alpha[i] % 2) {
            ans += i + 'A';
        }
    }

    //  'Z'부터 'A'까지 나온 알파벳의 개수/2만큼 알파벳을 정답변수 ans에 더해준다.
    for(int i=25; i>=0; i--) {
        for(int j=0; j<alpha[i]/2; j++) {
            ans += i + 'A';
        }
    }
    cout << ans;

    return 0;
}